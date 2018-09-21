from app import db


class Guest(db.Model):
    """Simple database model to track event attendees."""

    __tablename__ = 'passwords'
    id = db.Column(db.Integer, primary_key=True)
    hash = db.Column(db.LargeBinary)

    def __init__(self, hash=None):
        self.hash = hash

