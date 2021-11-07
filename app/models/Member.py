"""
Member model
"""

from app import db

class Member(db.Model):
    # table name in db
    __tablename__ = 'members'
    # primary key attribute
    id = db.Column(db.Integer(), primary_key=True)

    name = db.Column(db.Text(), nullable=False)
    email = db.Column(db.Text(), unique=True, nullable=False)
    notes = db.Column(db.Text(), nullable=True)
    phone_number = db.Column(db.Text(), nullable=True)
    free_status = db.Column(db.Boolean(), nullable=False)
    membership = db.Column(db.Text(), nullable=False)
    # navi
    # rentals = db.relationship('Rental', backref=db.backref('member'), cascade="all,delete")

    # init
    def __init__(self, **data):
        self.name = data.get('name', '')
        self.email = data.get('email', '')
        self.notes = data.get('notes', '')
        self.phone_number = data.get('phone_number', '')
        self.free_status = data.get('free_status', '')
        self.membership = data.get('membership', '')

        # represent

    def __repr__(self):
        return '{} - {}'.format(self.name, self.email)