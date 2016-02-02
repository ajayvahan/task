#!/usr/bin/python
"""verify username and password"""

import MySQLdb
import cgi, cgitb 
import smtplib
import json
# Create instance of FieldStorage 
form = cgi.FieldStorage() 
cgitb.enable()
db = MySQLdb.connect("localhost","root","mindfire","assignment")

# setup a cursor object using cursor() method
cursor = db.cursor()


login_username= form.getvalue('username')
login_password = form.getvalue('password')

print "Content-type:text/html\r\n\r\n"
print
response = dict()

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
        
            response.update({'success': False, 'message': "logging in", 'status':'active'})            
            print json.JSONEncoder().encode(response)
            fh=open('../../static/html_data/profile.txt')
            for line in fh:
                print ''.join(line).format(first_name,last_name,username,gender,dob,email,mobile,pk_id,image)
        else:
            # fh=open('../../static/html_data/login_message.txt')
            # for line in fh:
            #   print ''.join(line).format("Your account is not active")
            response.update({'success': True, 'message': "Your account is not active", 'status':'not active'})            
            print json.JSONEncoder().encode(response)
            
    else:
        # fh=open('../../static/html_data/login_error.txt')
        # for line in fh:
        #     print ''.join(line)
        response.update({'success': True, 'message': 'wrong username or password', 'status':'error'})
        print json.JSONEncoder().encode(response)

except Exception as e:
    # fh=open('../../static/html_data/login_message.txt')
    # for line in fh:
    #     print ''.join(line).format(e)
    response.update({'success': True, 'message': e, 'status': 'exception'})
    print json.JSONEncoder().encode(response)


# close the mysql database connection
db.close()
