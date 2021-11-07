"""
Configuration for Flask App
"""

from flask import Flask, url_for, current_app

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

# Importing all necessary API endpoints
from app import routes