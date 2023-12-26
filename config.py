#configuration file
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_uploads import IMAGES, UploadSet, configure_uploads, patch_request_class

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///shop.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
UPLOADED_PHOTOS_DEST = os.path.join(basedir, 'shop/static/images')
WTF_CSRF_ENABLED = True
SECRET_KEY = 'f2orget2oon1ey1ye0'

