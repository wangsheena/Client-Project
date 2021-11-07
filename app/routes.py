"""
API endpoints for Flask App
"""
import json

from app.application import app
from flask import jsonify, request, flash, redirect
from .models import Member


@app.route('/')
def index():
    return jsonify({'Status': 'Up'}), 200

@app.route('/Members')
def members():
    all_members = Member.query.all()
    return jsonify(all_members)