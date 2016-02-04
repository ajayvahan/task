#!/usr/bin/python
"""User authentication."""

import cgi
import cgitb
import json

import MySQLdb


def login():
    """Verify user and send feedback.

    Verify user name and password. If user exist, check status, if
    active open profile page else send feedback message.
    """
    cgitb.enable()

    # Create instance of FieldStorage
    form = cgi.FieldStorage()

    # Connecting to database
    db = MySQLdb.connect("localhost", "root", "mindfire", "assignment")

    # setup a cursor object using cursor() method
    cursor = db.cursor()

    # GET values from login form and assinging them in varables
    login_username = form.getvalue('username')
    login_password = form.getvalue('password')

    # HTTP header which is sent to the browser to understand the content.
    print "Content-type:text/html\r\n\r\n"
    print
    response = dict()

    # In this try block we handle any database error
    try:
        db1 = "SELECT pk_id FROM user_detail where username = '{0}' and \
                password = '{1}'".format(login_username, login_password)
        cursor.execute(db1)

        # If user exist then check weather account is active or not.
        if cursor.fetchone():
            db2 = "SELECT pk_id FROM user_detail where status='active' and \
                    username='{0}'".format(login_username)
            cursor.execute(db2)

            # If status is active the open user profile page
            if cursor.fetchone():
                db3 = "SELECT first_name,last_name,username,gender,dob,email,\
                        mobile,pk_id,image FROM user_detail where \
                            username='{0}'".format(login_username)
                cursor.execute(db3)

                for row in cursor.fetchall():
                    first_name = row[0]
                    last_name = row[1]
                    username = row[2]
                    gender = row[3]
                    dob = row[4]
                    email = row[5]
                    mobile = row[6]
                    pk_id = row[7]
                    image = row[8]

                response.update(
                    {'success': False, 'message': "logging in",
                     'status': 'active'})

                # open profile page through txt and passing value in the page
                fh = open('../../static/html_data/profile.txt')
                for line in fh:
                    print ''.join(line).format(
                        first_name, last_name, username, gender,
                        dob, email, mobile, pk_id, image)
            else:
                response.update(
                    {'success': True, 'message': "Your account is not active",
                     'status': 'not active'})
                print json.JSONEncoder().encode(response)
        else:
            response.update(
                {'success': True, 'message': 'wrong username or password',
                 'status': 'error'})
            print json.JSONEncoder().encode(response)

    except Exception as e:
        response.update({'success': True, 'message': e, 'status': 'exception'})
        print json.JSONEncoder().encode(response)

    # close the mysql database connection
    db.close()

# Calling login function
login()
