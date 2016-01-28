#!/usr/bin/python
"""To store user details and sending account activation email to the user"""

import MySQLdb
import cgi, cgitb
import smtplib
import datetime
import re
from validate_email import validate_email


# Create instance of FieldStorage 
form = cgi.FieldStorage() 

db = MySQLdb.connect("localhost","root","mindfire","assignment")

# setup a cursor object using cursor() method
cursor = db.cursor()


password = form.getvalue('password')
confirm_password  = form.getvalue('confirm_password')
first_name = form.getvalue('first_name')
last_name = form.getvalue('last_name')
gender = form.getvalue('gender')
dob = form.getvalue('dob')
mobile = form.getvalue('mobile')
email = form.getvalue('email')
username = form.getvalue('username')

print "Content-type:text/html\r\n\r\n"
print

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


# email validation
try:
    email_address = validate_email(email,verify=True)
except:
    email_address = 'False'



if first_name in [None, '', "N/A", 'NULL','None']:
    message="fill first name field"
    if gender=="male":
        male="checked"
    else:
        male=""
    if gender=="female":
        female="checked"
    else:
        female=""


    fh=open('../../static/html_data/signup_error.txt')
    for line in fh:
        print ''.join(line).format(first_name,last_name,username,male,female,dob,email,mobile,message)

elif last_name in [None, '', "N/A", 'NULL','None']:
    message="fill last name field"
    if gender=="male":
        male="checked"
    else:
        male=""
    if gender=="female":
        female="checked"
    else:
        female=""


    fh=open('../../static/html_data/signup_error.txt')
    for line in fh:
        print ''.join(line).format(first_name,last_name,username,male,female,dob,email,mobile,message)

elif first_name in [None, '', "N/A", 'NULL','None']:
    message="fill first name field"
    if gender=="male":
        male="checked"
    else:
        male=""
    if gender=="female":
        female="checked"
    else:
        female=""


    fh=open('../../static/html_data/signup_error.txt')
    for line in fh:
        print ''.join(line).format(first_name,last_name,username,male,female,dob,email,mobile,message)

elif username in [None, '', "N/A", 'NULL','None']:
    message="fill User name field"
    if gender=="male":
        male="checked"
    else:
        male=""
    if gender=="female":
        female="checked"
    else:
        female=""


    fh=open('../../static/html_data/signup_error.txt')
    for line in fh:
        print ''.join(line).format(first_name,last_name,username,male,female,dob,email,mobile,message)


elif password in [None, '', "N/A", 'NULL','None']:
    message="fill password field"
    if gender=="male":
        male="checked"
    else:
        male=""
    if gender=="female":
        female="checked"
    else:
        female=""


    fh=open('../../static/html_data/signup_error.txt')
    for line in fh:
        print ''.join(line).format(first_name,last_name,username,male,female,dob,email,mobile,message)

elif gender in [None, '', "N/A", 'NULL','None']:
    message="fill  gender field"
    if gender=="male":
        male="checked"
    else:
        male=""
    if gender=="female":
        female="checked"
    else:
        female=""


    fh=open('../../static/html_data/signup_error.txt')
    for line in fh:
        print ''.join(line).format(first_name,last_name,username,male,female,dob,email,mobile,message)

elif date=='false':
    message="fill date of birth in YYYY-MM-DD format"
    if gender=="male":
        male="checked"
    else:
        male=""
    if gender=="female":
        female="checked"
    else:
        female=""


    fh=open('../../static/html_data/signup_error.txt')
    for line in fh:
        print ''.join(line).format(first_name,last_name,username,male,female,dob,email,mobile,message)

elif phone in [None, '', "N/A", 'NULL','None']:
    message="invalid mobile number, please fill valid ten-digit mobile number"
    if gender=="male":
        male="checked"
    else:
        male=""
    if gender=="female":
        female="checked"
    else:
        female=""


    fh=open('../../static/html_data/signup_error.txt')
    for line in fh:
        print ''.join(line).format(first_name,last_name,username,male,female,dob,email,mobile,message)

elif email_address in [None, '', "N/A", 'NULL','None',False]:
    message="invalid email address, please fill valid email address"
    if gender=="male":
        male="checked"
    else:
        male=""
    if gender=="female":
        female="checked"
    else:
        female=""


    fh=open('../../static/html_data/signup_error.txt')
    for line in fh:
        print ''.join(line).format(first_name,last_name,username,male,female,dob,email,mobile,message)













#confirmation of password and then insert user data in columns
elif password == confirm_password:
    

    #inserting user data in user_detail table
    try:
        sql="INSERT INTO user_detail(first_name,last_name,gender,dob,mobile,email,username,password,status)\
         VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','inactive')"\
         .format(first_name,last_name,gender,dob,mobile,email,username,password)
        cursor.execute(sql)
        db.commit()
        
        # retrieving the pk_id from user_detail
        try:            
            cursor_id = db.cursor()
            sql_id = "SELECT pk_id FROM user_detail where username = '{0}'".format(username)
            cursor_id.execute(sql_id)
            pk_id_tuple = cursor_id.fetchone()

            pk_id=pk_id_tuple[0]
            

            # sending activation link to user email address
            to = '{0}'.format(email)
            sender = 'ajay.vahan@mindfiresolutions.com'
            sender_password = '1mfmail2016#'
            subject = 'Activation Email'
            # writing content to send in mail
            text="""Activate your account by

                    <a href="http://localhost/cgi-bin/app/activate.py?id={0}">Clicking here</a>
                    """.format(pk_id)

            server = smtplib.SMTP('email.mindfiresolutions.com',587)
            server.ehlo()
            server.starttls()
            server.login(sender,sender_password)

            body = '\r\n'.join([
                    'To: {0}'.format(email),
                    'From: {0}'.format(sender),
                    'Subject: {0}'.format(subject),
                    'MIME-Version: 1.0',
                    'Content-type: text/html'
                    '',
                    text
                    ])

            #sending email to user
            try:
                server.sendmail(sender,[to],body)
                fh=open('../../static/html_data/message.txt')
                for line in fh:
                    print ''.join(line).format("You have registered successfully","Activation link is sent to your mail")

            except Exception as e:
                message=e
                if gender=="male":
                    male="checked"
                else:
                    male=""
                if gender=="female":
                    female="checked"
                else:
                    female=""


                fh=open('../../static/html_data/signup_error.txt')
                for line in fh:
                    print ''.join(line).format(first_name,last_name,username,male,female,dob,email,mobile,message)
            # sending email end

        except Exception as e:
            message=e
            if gender=="male":
                male="checked"
            else:
                male=""
            if gender=="female":
                female="checked"
            else:
                female=""


            fh=open('../../static/html_data/signup_error.txt')
            for line in fh:
                print ''.join(line).format(first_name,last_name,username,male,female,dob,email,mobile,message)


    except Exception as e:
        db.rollback()
        message=e
        if gender=="male":
            male="checked"
        else:
            male=""
        if gender=="female":
            female="checked"
        else:
            female=""


        fh=open('../../static/html_data/signup_error.txt')
        for line in fh:
            print ''.join(line).format(first_name,last_name,username,male,female,dob,email,mobile,message)


else:
    message="password didn't match"
    if gender=="male":
        male="checked"
    else:
        male=""
    if gender=="female":
        female="checked"
    else:
        female=""


    fh=open('../../static/html_data/signup_error.txt')
    for line in fh:
        print ''.join(line).format(first_name,last_name,username,male,female,dob,email,mobile,message)



# closing the mysql database connection
db.close()