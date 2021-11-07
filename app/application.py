"""
Configuration for Flask App
"""
import os

from flask import Flask, url_for, current_app
import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres://jeethajxhrruzl:6dd02f314f29f7701cf0e7f6aaa7d910322f5995aaa9fd180dfb1cc8d31c2cb6@ec2-52-86-223-172.compute-1.amazonaws.com:5432/dakd6qc062hna5"
os.environ['DATABASE_URL']
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)

# Importing all necessary API endpoints
from app import routes