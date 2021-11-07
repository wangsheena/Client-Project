"""
API endpoints for Flask App
"""
import json

from app.application import app
from flask import jsonify, request, flash, redirect


@app.route('/')
def index():
    return jsonify({'Status': 'Up'}), 200