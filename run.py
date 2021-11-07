"""
Flask initialization
Server entry-point
"""

from app.application import app

if __name__ == '__main__':
    app.run(debug=True)
