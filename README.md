# wall-back
Python/Django app, virtual environment created with: <br/> 
`python3 -m venv env`

##### Start virtual environment
from the root directory: <br/>
`source env/bin/activate`

##### Once in virtual is started, packages may need to be installed: 
`pip install django`<br/>
`pip install djangorestframework`<br/>
`pip install python-dotenv`<br/>
`pip install django-cors-headers`<br/>
`pip install django-allauth`<br/>
`pip install django-rest-auth`<br/>

##### Start server
cd into /thewall directory: <br/>
`python manage.py runserver`<br/>
(may need python3)<br/>


When switching computers ran into a few missing installations:<br/>
sudo apt install python-pip<br/>
sudo apt-get install python3-venv (was a Debian/Ubuntu error)<br/>
sudo apt-get install python3-django <br/>


In case some issues come up with environment these were my original local environment and package settings:<br/>
System: Ubuntu 20.04<br/>
Python: command not available<br/>
Python3: Python 3.8.5<br/>
Django: 3.1.1<br/>
django-allauth: 0.42.0<br/>
django-cors-headers: 3.5.0<br/>
djangorestframework: 3.11.1<br/>
python-dotenv: 0.14.0<br/>
pip: 20.0.2<br/>

Trouble with dotenv in settings.py from another computer, so commented out:<br/>
from dotenv import load_dotenv<br/>
load_dotenv()<br/>

Was to store .env email settings, but switched EMAIL_BACKEND settings just for testing:<br/>
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
