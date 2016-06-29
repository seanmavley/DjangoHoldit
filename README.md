A simple django application for serving placeholder images similar to Placehold.it . 
See working instance online: http://i.kkhophi.co 

Its great for working when in offline mode, on your local PC.

# Features
All Placehold.it does, with an extra flavor of easy offline setup and use.

# How to use?
Visit http://i.khophi.co/ to see working example.

# Steps to host locally
 - Download the source of the Django Hold It from Github.
 - Extract .zip file
 - Open your terminal and change directory to the extracted folder, so something like cd ~/Downloads/djangoholdit/
 - In terminal, run `sudo pip install -r requirements.txt`
 - Then start the server by typing `python manage.py runserver`
 - Visit your localhost in your browser to see in action

# Running tests
 - You must have the server running on localhost:8000
 - You must have the chromedriver file in ~/home/khophi/Downloads/ folder. Otherwise, change the resource to point to the respective directory you have yours in.
 - In the root folder, `python manage test`

Contact
=======
Want to get in touch? Here: hello@khophi.co

Support
=======
Django Hold it is supported by TheAfricanDream.co

License
=======
See License File
