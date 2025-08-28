import os
import sys

# Add your project directory to the sys.path
path = '/home/shazoo/pythonCrud'
if path not in sys.path:
    sys.path.append(path)

# Set the settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'pythonCrud.settings'  # 👈 yahan apne project ka settings path likho

# Get WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
