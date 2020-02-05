"""
WSGI config for MII project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
from dj_static import Cling
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MII.settings')

# application = get_wsgi_application()

application = Cling(get_wsgi_application())

if os.getcwd() == 'app':
  from whitenoise.django import DjangoWhiteNoise 
  application = DjangoWhiteNoise(application)