#!/usr/bin/python
"""Server side validation."""


import cgi
import datetime
import os
import re
import uuid

import MySQLdb


def edit():
    """Validate, update and send feedback.

    Validate every field before updating in database and send feedback
    and if correct update corresponding column's in database and if
    uploaded image, writing the image file to the server directory and
    storing the image path in database.
    """
    # Create instance of FieldStorage
    form = cgi.FieldStorage()

    # Connecting to database
    db = MySQLdb.connect("localhost", "root", "mindfire", "assignment")

    # setup a cursor object using cursor() method
    cursor = db.cursor()

    # A nested FieldStorage instance holds the file
    fileitem = form['image']

    try:    # Windows needs stdio set for binary mode.
        import msvcrt
        msvcrt.setmode(0, os.O_BINARY)  # stdin  = 0
        msvcrt.setmode(1, os.O_BINARY)  # stdout = 1
    except ImportError:
        pass

    # GET values from edit form and assinging them in varables
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
    zip_number = zip_code
    q = re.compile('(^[0-9]{6}$)')
    try:
        zipcode = q.match(zip_number)
    except:
        zipcode = ''

    # HTTP header which is sent to the browser to understand the content.
    print "Content-type:text/html\r\n\r\n"
    print

    try:
        sql = "SELECT image FROM user_detail WHERE pk_id={0}".format(pk_id)
        cursor.execute(sql)
        for row in cursor.fetchall():
            image = row[0]
    except Exception as e:
        print e

    # Check marital dropdown and if selected assigning them to variables
    if marital == "single":
        single = "selected"
    else:
        single = " "

    if marital == "married":
        married = "selected"
    else:
        married = " "

    # Check gender radio field and if checked assigng them to variables
    if gender == "male":
        male = "checked"
    else:
        male = " "

    if gender == "female":
        female = "checked"
    else:
        female = " "

    # Check employment dropdown and if selected assigning them to variables
    if employment == "student":
        student = "selected"
    else:
        student = " "

    if employment == "working":
        working = "selected"
    else:
        working = " "

    if employment == "not working":
        not_working = "selected"
    else:
        not_working = " "

    # Checking First name feild
    if first_name in [None, '', "N/A", 'NULL', 'None']:
        message = " Fill first name field"

        # open edit2.txt page and passing value in the page
        fh = open('../../static/html_data/edit2.txt')
        for line in fh:
            print ''.join(line).format(
                first_name, last_name, male, female, dob, mobile, single,
                married, student, working, not_working, address, street,
                city, zip_code, pk_id, image, "danger", "Error!", message)

    # Checking Last name feild
    elif last_name in [None, '', "N/A", 'NULL', 'None']:
        message = " Fill last name field"

        # open edit2.txt page and passing value in the page
        fh = open('../../static/html_data/edit2.txt')
        for line in fh:
            print ''.join(line).format(
                first_name, last_name, male, female, dob, mobile, single,
                married, student, working, not_working, address, street,
                city, zip_code, pk_id, image, "danger", "Error!", message)

    # Checking Gender feild
    elif gender in [None, '', "N/A", 'NULL', 'None']:
        message = " Fill gender field"

        # open edit2.txt page and passing value in the page
        fh = open('../../static/html_data/edit2.txt')
        for line in fh:
            print ''.join(line).format(
                first_name, last_name, male, female, dob, mobile, single,
                married, student, working, not_working, address, street,
                city, zip_code, pk_id, image, "danger", "Error!", message)

    # Checking Date of birth feild
    elif date == 'false':
        message = " Fill date of birth in YYYY-MM-DD format"

        # open edit2.txt page and passing value in the page
        fh = open('../../static/html_data/edit2.txt')
        for line in fh:
            print ''.join(line).format(
                first_name, last_name, male, female, dob, mobile, single,
                married, student, working, not_working, address, street,
                city, zip_code, pk_id, image, "danger", "Error!", message)

    # Checking Mobile feild
    elif phone in [None, '', "N/A", 'NULL', 'None']:
        message = " Invalid mobile number, please\
         fill valid ten-digit mobile number"

        # open edit2.txt page and passing value in the page
        fh = open('../../static/html_data/edit2.txt')
        for line in fh:
            print ''.join(line).format(
                first_name, last_name, male, female, dob, mobile, single,
                married, student, working, not_working, address, street,
                city, zip_code, pk_id, image, "danger", "Error!", message)

    # Checking city feild
    elif city in [None, '', "N/A", 'NULL', 'None']:
        message = " Fill city field"

        # open edit2.txt page and passing value in the page
        fh = open('../../static/html_data/edit2.txt')
        for line in fh:
            print ''.join(line).format(
                first_name, last_name, male, female, dob, mobile, single,
                married, student, working, not_working, address, street,
                city, zip_code, pk_id, image, "danger", "Error!", message)

    # Checking zip-code feild
    elif zipcode in [None, '', "N/A", 'NULL', 'None']:
        message = " Invalid zipcode, please fill valid six-digit zip code"

        # open edit2.txt page and passing value in the page
        fh = open('../../static/html_data/edit2.txt')
        for line in fh:
            print ''.join(line).format(
                first_name, last_name, male, female, dob, mobile, single,
                married, student, working, not_working, address, street,
                city, zip_code, pk_id, image, "danger", "Error!", message)

    else:
        try:
            sql = "UPDATE user_detail SET first_name='{0}',last_name='{1}',\
            gender='{2}',dob='{3}',mobile='{4}',marital='{5}',employment='{6}',\
            address='{7}',street='{8}',city='{9}',zip='{10}'\
             WHERE pk_id='{11}'".format(
                first_name, last_name, gender, dob, mobile,
                marital, employment, address, street, city,
                zip_code, pk_id)
            cursor.execute(sql)
            db.commit()

        except Exception as e:

            fh = open('../../static/html_data/message.txt')
            for line in fh:
                print ''.join(line).format("Oops... Error", e)

        if fileitem.filename:

            # strip leading path from file name
            # to avoid directory traversal attacks
            fn = os.path.basename(fileitem.filename)

            # writing the file to the server directory
            unique_name = uuid.uuid4().fields[0]
            open('../../static/images/{0}{1}'.format(
                unique_name, fn), 'wb').write(fileitem.file.read())
            path = "/static/images/{0}{1}".format(unique_name, fn)

            # storing the image path to database
            try:
                sql_image = "UPDATE user_detail SET image='{0}'\
                 WHERE pk_id='{1}'".format(path, pk_id)
                cursor.execute(sql_image)
                db.commit()
                message = "Successfully Updated the details\
                 and uploaded the image"

                # open edit2.txt page and passing value in the page
                fh = open('../../static/html_data/edit2.txt')
                for line in fh:
                    print ''.join(line).format(
                        first_name, last_name, male, female, dob,
                        mobile, single, married, student, working,
                        not_working, address, street, city,
                        zip_code, pk_id, image,
                        "success", "Success!", message)

            except Exception as e:
                db.rollback()
                message = e

                # open edit2.txt page and passing value in the page
                fh = open('../../static/html_data/edit2.txt')
                for line in fh:
                    print ''.join(line).format(
                        first_name, last_name, male, female, dob,
                        mobile, single, married, student, working,
                        not_working, address, street, city,
                        zip_code, pk_id, image,
                        "danger", "Error!", message)

        else:
            message = "Successfully Updated"

            # open edit2.txt page and passing value in the page
            fh = open('../../static/html_data/edit2.txt')
            for line in fh:
                print ''.join(line).format(
                    first_name, last_name, male, female, dob, mobile, single,
                    married, student, working, not_working, address, street,
                    city, zip_code, pk_id, image,
                    "success", "Success!", message)

    # close the mysql database connection
    db.close()

# Calling edit function
edit()
