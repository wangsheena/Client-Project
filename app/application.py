"""
Configuration for Flask App
"""
import os

from flask import Flask, url_for, current_app
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)

# Importing all necessary API endpoints
from app import routes