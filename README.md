DjangoHoldit
============
A simple django application for serving placeholder images similar to Placehold.it . 
See working instance online: http://djangoholdit.herokuapp.com/ Its great for working when in offline mode, on your local PC.

Features
========
* Displays image as per dimension specified from url like http://url.com/100x100/
* Displays image in a specified color as per appending the /as/<RGB_values> like http://url.com/100x100/as/10.10.10/

How to use?
===========
Visit http://djangoholdit.herokuapp.com/100x100/ to see an example. Append the dimension you want displayed to the URL, in the format, <number>x<number>. If using instance of the app locally (or on your PC), simply append the dimension to your localhost address like so: http://localhost:<port>/100x100/

Steps to host locally
======================
This is a django app, so surely, django is needed. I worked on in django 1.7 final, so you might wanna stick to that version or higher. 

1. Clone this repository
2. Change DEBUG = False in Placeholder/settings.py to Debug = True 
3. In the project root folder (where the manage.py is), start your development server. Hook it to a port other than the default 8000, so you can use it alongside other apps that might be using the 8000 already.
4. Have fun.

Steps to host online
=====================
Placehold.it works best and this app is not to replace it. I came up with this app to use for local purposes mainly. However if you wish to host it online, you're free to.

Contact
=======
http://google.com/+Nkansahrexford

License
=======
Python License
