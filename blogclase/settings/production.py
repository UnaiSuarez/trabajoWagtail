from .base import *

DEBUG = False

SECRET_KEY = 'isjdfyu6672hfkguieyljokrzvvwsydc&2d+_d6wd+t#eo2+t*ie3!cnt4ksdw!me9*%i'

# ARREGLAR
ALLOWED_HOSTS = ['*'] 


DATABASES = {
  "default": {
    "ENGINE": "django.db.backends.postgresql",
    "NAME": "blogclase",
    "USER": "usuario",
    "PASSWORD": "password",
    "HOST": "localhost",
    "PORT": "5432",
  }
}

try:
    from .local import *
except ImportError:
    pass
