#!/usr/bin/python
"""Forgot password."""

import cgi
import smtplib

import MySQLdb


def forgot():
    """Verify user and send email.

    Verify user email, If exist send user name and password to
    corresponding email,
    """
    # Create instance of FieldStorage
    form = cgi.FieldStorage()

    # Connecting to database
    db = MySQLdb.connect("localhost", "root", "mindfire", "assignment")

    # setup a cursor object using cursor() method
    cursor = db.cursor()

    sender_email = form.getvalue('email')

    sender = 'ajay.vahan@mindfiresolutions.com'
    sender_password = '1mfmail2016#'

    subject = 'Password Recovery Email'
    username = ''
    password = ''

    print "Content-type:text/html\r\n\r\n"
    print
    print '<html>'
    print '<head>'
    print '<title>forgot page</title>'
    print '</head>'
    print '<body>'

    sql = "SELECT IF( EXISTS(SELECT pk_id FROM user_detail\
     WHERE email='{0}') ,1,0)".format(sender_email)
    cursor.execute(sql)
    check_tuple = cursor.fetchone()
    check = check_tuple[0]

    if check == 1:
        try:
            cursor.execute("SELECT username,password FROM user_detail\
             WHERE email='{0}'".format(sender_email))
            for row in cursor.fetchall():
                username = row[0]
                password = row[1]

            text = """username = {0} \r\npassword = {1}""".format(
                username, password)

            server = smtplib.SMTP('email.mindfiresolutions.com', 587)
            server.ehlo()
            server.starttls()
            server.login(sender, sender_password)

            body = '\r\n'.join([
                'To: {0}'.format(sender_email),
                'From: {0}'.format(sender),
                'Subject: {0}'.format(subject),
                '',
                text])

            try:
                server.sendmail(sender, [sender_email], body)

                # open message.txt and passing value in the page
                fh = open('../../static/html_data/message.txt')
                for line in fh:
                    print ''.join(line).format(
                        "You can find your account now",
                        "Username and password is sent to your email address")

            except Exception as e:

                # open message.txt and passing value in the page
                fh = open('../../static/html_data/forgot_error.txt')
                for line in fh:
                    print ''.join(line).format(e)

        except Exception as e:

            # open message.txt and passing value in the page
            fh = open('../../static/html_data/forgot_error.txt')
            for line in fh:
                print ''.join(line).format(e)
        server.quit()

    else:

        # open message.txt and passing value in the page
        fh = open('../../static/html_data/forgot_error.txt')
        for line in fh:
            print ''.join(line).format(
                "Email does not exist,\
                please enter the email with which you registered")

    print '</body>'
    print '</html>'

    # close the mysql database connection
    db.close()

# Calling forgot() function
forgot()
