#!/usr/bin/python
"""To store user details and sending acountemail to the user"""

import MySQLdb
import cgi,os
import cgitb; cgitb.enable()
import uuid
import smtplib
import datetime
import re

# Create instance of FieldStorage
form = cgi.FieldStorage()

db = MySQLdb.connect("localhost","root","mindfire","assignment")

# setup a cursor object using cursor() method
cursor = db.cursor()

# A nested FieldStorage instance holds the file
fileitem = form['image']

# Windows needs stdio set for binary mode.
try:
	import msvcrt
	msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
	msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
	pass



first_name = form.getvalue('first_name')
last_name = form.getvalue('last_name')
gender = form.getvalue('gender')
dob = form.getvalue('dob')
mobile = form.getvalue('mobile')
marital = form.getvalue('marital')
employment = form.getvalue('employment')
address = form.getvalue('address')
street = form.getvalue('street')
city = form.getvalue('city')
zip_code = form.getvalue('zip')
pk_id = form.getvalue('pk_id')


# validating date
try:
    datetime.datetime.strptime(dob, '%Y-%m-%d')
    date = 'true'
except:
    date = 'false'


# validating mobile number
phone_number = mobile
p = re.compile('(^[0-9]{10}$)')
try:
    phone = p.match(phone_number)
except:
    phone = ''

# validating zipcode
zip_number= zip_code
q = re.compile('(^[0-9]{6}$)')
try:
    zipcode = q.match(zip_number)
except:
    zipcode= ''

print "Content-type:text/html\r\n\r\n"
print

try:
	sql="SELECT image FROM user_detail WHERE pk_id={0}".format(pk_id)
	cursor.execute(sql)
	for row in cursor.fetchall():
		image=row[0]
except Exception as e:
	print e

if marital=="single":
	single="selected"
else:
	single=" "

if marital=="married":
	married="selected"
else:
	married=" "

if gender=="male":
	male="checked"
else:
	male=" "

if gender=="female":
	female="checked"
else:
	female=" "

if employment=="student":
	student="selected"
else:
	student=" "

if employment=="working":
	working="selected"
else:
	working=" "

if employment=="not working":
	not_working="selected"
else:
	not_working=" "

if first_name in [None, '', "N/A", 'NULL','None']:
	message=" Fill first name field"
	fh=open('../../static/html_data/edit2.txt')
	for line in fh:
		print ''.join(line).format(first_name,last_name,male,female,dob,mobile,single,married,student,working,not_working,address,street,city,zip_code,pk_id,image,"danger","Error!",message)

elif last_name in [None, '', "N/A", 'NULL','None']:
	message=" Fill last name field"
	fh=open('../../static/html_data/edit2.txt')
	for line in fh:
		print ''.join(line).format(first_name,last_name,male,female,dob,mobile,single,married,student,working,not_working,address,street,city,zip_code,pk_id,image,"danger","Error!",message)

elif gender in [None, '', "N/A", 'NULL','None']:
	message=" Fill gender field"
	fh=open('../../static/html_data/edit2.txt')
	for line in fh:
		print ''.join(line).format(first_name,last_name,male,female,dob,mobile,single,married,student,working,not_working,address,street,city,zip_code,pk_id,image,"danger","Error!",message)


elif date=='false':
	message=" Fill date of birth in YYYY-MM-DD format"
	fh=open('../../static/html_data/edit2.txt')
	for line in fh:
		print ''.join(line).format(first_name,last_name,male,female,dob,mobile,single,married,student,working,not_working,address,street,city,zip_code,pk_id,image,"danger","Error!",message)

elif phone in [None, '', "N/A", 'NULL','None']:
	message=" Invalid mobile number, please fill valid ten-digit mobile number"
	fh=open('../../static/html_data/edit2.txt')
	for line in fh:
		print ''.join(line).format(first_name,last_name,male,female,dob,mobile,single,married,student,working,not_working,address,street,city,zip_code,pk_id,image,"danger","Error!",message)

elif city in [None, '', "N/A", 'NULL','None']:
	message=" Fill city field"
	fh=open('../../static/html_data/edit2.txt')
	for line in fh:
		print ''.join(line).format(first_name,last_name,male,female,dob,mobile,single,married,student,working,not_working,address,street,city,zip_code,pk_id,image,"danger","Error!",message)

elif zipcode in [None, '', "N/A", 'NULL','None']:
	message=" Invalid zipcode, please fill valid six-digit zip code"
	fh=open('../../static/html_data/edit2.txt')
	for line in fh:
		print ''.join(line).format(first_name,last_name,male,female,dob,mobile,single,married,student,working,not_working,address,street,city,zip_code,pk_id,image,"danger","Error!",message)

else:
	try:
		sql="UPDATE user_detail SET first_name='{0}',last_name='{1}',gender='{2}',dob='{3}',\
		mobile='{4}',marital='{5}',employment='{6}',address='{7}',street='{8}',city='{9}',zip='{10}'\
		 WHERE pk_id='{11}'".format(first_name,last_name,gender,dob,mobile,marital,employment,address,street,city,zip_code,pk_id)
		cursor.execute(sql)
		db.commit()

		# message="Successfully Updated"
		# fh=open('../../static/html_data/edit2.txt')
		# for line in fh:
		# 	print ''.join(line).format(first_name,last_name,male,female,dob,mobile,single,married,student,working,not_working,address,street,city,zip_code,pk_id,image,"success","Success!",message)


		
	except Exception as e:
		fh=open('../../static/html_data/message.txt')
		for line in fh:
			print ''.join(line).format("Oops... Error",e)





	if fileitem.filename:
		# strip leading path from file name to avoid directory traversal attacks
		fn = os.path.basename(fileitem.filename)
		# writing the file to the server directory
		unique_name=uuid.uuid4().fields[0]
		open('../../static/images/{0}{1}'.format(unique_name,fn), 'wb').write(fileitem.file.read())
		path="/static/images/{0}{1}".format(unique_name,fn)

		# storing the image path to database
		try:
			sql_image="UPDATE user_detail SET image='{0}' WHERE pk_id='{1}'".format(path,pk_id)
			cursor.execute(sql_image)
			db.commit()
			message="Successfully Updated the details and uploaded the image"
			fh=open('../../static/html_data/edit2.txt')
			for line in fh:
				print ''.join(line).format(first_name,last_name,male,female,dob,mobile,single,married,student,working,not_working,address,street,city,zip_code,pk_id,image,"success","Success!",message)




		except Exception as e:
			db.rollback()
			message=e
			fh=open('../../static/html_data/edit2.txt')
			for line in fh:
				print ''.join(line).format(first_name,last_name,male,female,dob,mobile,single,married,student,working,not_working,address,street,city,zip_code,pk_id,image,"success","Success!",message)



			fh=open('../../static/html_data/message.txt')
			for line in fh:
				print ''.join(line).format("Error in uploading image",e)


	else:
		message="Successfully Updated"
		fh=open('../../static/html_data/edit2.txt')
		for line in fh:
			print ''.join(line).format(first_name,last_name,male,female,dob,mobile,single,married,student,working,not_working,address,street,city,zip_code,pk_id,image,"success","Success!",message)






# close the mysql database connection
db.close()
