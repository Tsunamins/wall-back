# wall-back
Python/Django app, virtual environment created with: `python3 -m venv env`


##### Start virtual environment
from the root directory: 
`source env/bin/activate`

##### Once in virtual is started, packages may need to be installed: 
`pip install django`
`pip install djangorestframework`
`pip install python-dotenv`
`pip install django-cors-headers`
`pip install django-allauth`
`pip install django-rest-auth`

##### Start server
cd into /thewall directory: 
`python manage.py runserver`
(may need python3)


When switching computers ran into a few missing installations:
may need first: sudo apt install python-pip
and: sudo apt-get install python3-venv (was a Debian/Ubuntu error)
also: sudo apt-get install python3-django


In case some issues come up with environment these were my original local environment settings:
System: Ubuntu 20.04
Python: command doesn't work
Python3: Python 3.8.5
Django: 3.1.1
django-allauth: 0.42.0
django-cors-headers: 3.5.0
djangorestframework: 3.11.1
python-dotenv: 0.14.0
pip: 20.0.2

Trouble with dotenv in settings.py from another computer, so commented out:
from dotenv import load_dotenv
load_dotenv()

Was to store .env email settings, but switched EMAIL_BACKEND settings just for testing:
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
