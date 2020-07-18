from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from tiny0.config import SECRET_KEY, SQLALCHEMY_DATABASE_URI

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)

from tiny0 import routes
