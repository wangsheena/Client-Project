"""
Admin model for database
"""

import SQLAlchemy


db = SQLAlchemy()


class Admin(db.Model):
    """
    Admin accounts
    """
    # ___tablename___ = 'admins'

    name = db.StringField()
    password = db.StringField()

    def to_json(self):
        return({'name': self.name})

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)