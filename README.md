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




When switching computers ran into a few missing installations:
may need first: sudo apt install python-pip
and: sudo apt-get install python3-venv (was a Debian/Ubuntu error)
also: sudo apt-get install python3-django