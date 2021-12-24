import os
from distutils.util import strtobool

WEBSITE_DOMAIN = os.environ.get("WEBSITE_DOMAIN")
if not WEBSITE_DOMAIN:
	WEBSITE_DOMAIN = "127.0.0.1:5000"

SECRET_KEY = os.environ.get("SECRET_KEY")
if not SECRET_KEY:
	SECRET_KEY = "SECRET_KEY"

SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
if not SQLALCHEMY_DATABASE_URI:
	SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"

DEBUG = os.environ.get("DEBUG")
if not DEBUG:
	DEBUG = "true"

DEBUG = strtobool(DEBUG)
