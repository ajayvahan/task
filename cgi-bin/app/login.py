#!/usr/bin/python
"""verify username and password"""

import MySQLdb
import cgi, cgitb 
import smtplib

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

db = MySQLdb.connect("localhost","root","mindfire","assignment")

# setup a cursor object using cursor() method
cursor = db.cursor()


login_username= form.getvalue('username')
login_password = form.getvalue('password')

print "Content-type:text/html\r\n\r\n"
print


try:

	db1 = "SELECT pk_id FROM user_detail where username = '{0}' and password = '{1}'".format(login_username,login_password)
	cursor.execute(db1)

	if cursor.fetchone():

		db2="SELECT pk_id FROM user_detail where status='active' and username='{0}'".format(login_username)
		cursor.execute(db2)
		if cursor.fetchone():
			db3="SELECT first_name,last_name,username,gender,dob,email,mobile,pk_id,image FROM user_detail where username='{0}'".format(login_username)
			cursor.execute(db3)

			for row in cursor.fetchall():
				first_name=row[0]
				last_name=row[1]
				username=row[2]
				gender=row[3]
				dob=row[4]
				email=row[5]
				mobile=row[6]
				pk_id=row[7]
				image=row[8]
		

			fh=open('../../static/html_data/profile.txt')
			for line in fh:
				print ''.join(line).format(first_name,last_name,username,gender,dob,email,mobile,pk_id,image)
		else:
			fh=open('../../static/html_data/login_message.txt')
			for line in fh:
				print ''.join(line).format("Your account is not active")
			
	else:
		fh=open('../../static/html_data/login_error.txt')
		for line in fh:
			print ''.join(line)
			
		
except Exception as e:
	fh=open('../../static/html_data/login_message.txt')
	for line in fh:
		print ''.join(line).format(e)


# close the mysql database connection
db.close()