from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'J5iRz4FDEJS7QnTZmadh'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///alumnos.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
