"""
API endpoints for Flask App
"""
import json

from app.application import app
from flask import jsonify, request, flash, redirect
from flask.ext.login import current_user, LoginManager, login_user, logout_user, login_required
from flask_mongoengine import MongoEngine


@app.route('/')
def index():
    return jsonify({'Status': 'Up'}), 200

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
@app.route('/login', methods=['POST'])
def login():
    req = json.loads(request.data)
    username = req.get('username', 'guest')
    password = req.get('password', '')
    user = User.objects(name=username, password=password).first() # Create as user object

    # Check for user object
    if user:
        login_user(user)
        return jsonify(user.to_json())
    else:
        return jsonify({'status': 401,
                        'reason': "Username and password do not match"})
