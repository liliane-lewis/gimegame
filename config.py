__author__ = 'liliane'
# coding: utf-8

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


# configuração
DATABASE = 'db/gimegame.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'


app = Flask(__name__)
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/gimegame.db'

db = SQLAlchemy(app)

app.config.from_envvar('CONFIG_FLASKR', silent=True)

