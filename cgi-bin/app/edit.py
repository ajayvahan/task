#!/usr/bin/python
"""Edit profile page"""

import MySQLdb
import cgi, cgitb 
import smtplib

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

db = MySQLdb.connect("localhost","root","mindfire","assignment")

# setup a cursor object using cursor() method
cursor = db.cursor()


pk_id= form.getvalue('pk_id')


print "Content-type:text/html\r\n\r\n"
print

try:
	sql="SELECT  first_name,last_name,gender,dob,mobile,marital,employment,address,street,city,zip,image FROM user_detail WHERE pk_id={0}".format(pk_id)
	cursor.execute(sql)

	for row in cursor.fetchall():
		first_name=row[0]
		last_name=row[1]
		gender=row[2]
		dob=row[3]
		mobile=row[4]
		marital=row[5]
		employment=row[6]
		address=row[7]
		street=row[8]
		city=row[9]
		zip_code=row[10]
		image=row[11]

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





	




	
	fh=open('../../static/html_data/edit.txt')
	for line in fh:
		print ''.join(line).format(first_name,last_name,male,female,dob,mobile,single,married,student,working,not_working,address,street,city,zip_code,pk_id,image)

except Exception as e:
	fh=open('../../static/html_data/message.txt')
	for line in fh:
		print ''.join(line).format("Oops... Error",e)

# close the mysql database connection
db.close()