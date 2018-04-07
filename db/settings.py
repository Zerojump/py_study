import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

SECRET_KEY = '123'

INSTALLED_APPS = [
    "django_orm"
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django',
        'USER': 'ruby',
        'PASSWORD': 'ruby',
        'HOST': '192.168.47.128',
        'PORT': '3306'
    }
}
