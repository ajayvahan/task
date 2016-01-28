#!/usr/bin/python
"""Activates the user by changing the status column in the database from 'inactive' to 'active'"""

import MySQLdb
import cgi, cgitb

form = cgi.FieldStorage()

# connect to the database
db = MySQLdb.connect("localhost","root","mindfire","assignment")

# setup a cursor object using cursor() method
cursor = db.cursor()
pk_id = form.getvalue('id')

print "Content-type:text/html\r\n\r\n"
print
print '<html>'
print '<head>'
print '<title>Activation page</title>'
print '</head>'
print '<body>'


# activating the account by changing status to active
try:
	sql= "UPDATE user_detail SET status='active' where pk_id = {0}".format(pk_id)
	cursor.execute(sql)
	
	fh=open('../../static/html_data/message.txt')
	for line in fh:
		print ''.join(line).format("Your account is active",'Please <a href="http://localhost/static/html/login.html">click here</a> to continue')

	db.commit()
except Exception as e:
	fh=open('../../static/html_data/message.txt')
	for line in fh:
		print ''.join(line).format("Error in activation",e)

	db.rollback()

print '</body>'
print '</html>'

# close the mysql database connection
db.close()