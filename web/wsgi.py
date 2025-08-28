import os
import sys

# add project directory to sys.path
path = '/home/shazoo/pythonCrud'
if path not in sys.path:
    sys.path.append(path)

# set DJANGO_SETTINGS_MODULE
os.environ['DJANGO_SETTINGS_MODULE'] = 'ecommerce.settings'

# get WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
