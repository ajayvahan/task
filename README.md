Assignment - Login, signup, and profile page.
=============================================
Descripton:
===========
Application allow user to register thier details and on successfull registeration, account activation link is sent to user and on clicking that link user actives thier account. In login page user authentication is done on basis of username, password, and status weather account is active or not. If user verification is done successfully then user login to thier profile page where user is provided with edit profile option. On clicking edit profile, user is redirected to edit profile page where user can edit their details and can also upload thier profile picture and this application also has the feature of recovering the user account in case if user forgets their password, it verify user email and send username and password to thier mail. In all pages every fields are validated both on client side as well as server side, if validation is correct, save the changes to database and send feedback to user. 

Technologies used:
==================
Frontend:
---------
HTML, CSS, Bootstrap, JS, Jquery, Ajax

Backend:
--------
Core Python, MySQL

Note: Please keep the 'cgi-bin' and 'static' folder inside '/var/www/html/' directory and make 
sure that your Web Server supports CGI and it is configured to handle CGI Programs.

Packages reqiured to run:
-----------------------

1. MySQLdb
2. cgi
3. validate_email

path required to run in terminal:
------------------------------

 1.for python files:
    
    /var/www/html/cgi-bin/app/filename.py

2.for html,html_data

    /var/www/html/static/html/filename.html
   
path reqiured to run in browser:
---------------------------------

   http://localhost/static/html/login.html
 
 
CGI configuration :-
---------------------------------------------------
serve-cgi-bin.conf

	< Directory "/var/www/html/cgi-bin" >
		AddHandler cgi-script .cgi .py
		AllowOverride None
		Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
		Require all granted
	< /Directory >
  

 
