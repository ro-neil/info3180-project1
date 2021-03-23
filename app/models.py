from . import db
from flask_login._compat import unicode

# Requires client-side validation

class Property(db.Model):
    __tablename__ = 'properties'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('Title',db.String(80))
    description = db.Column('Description',db.String(255))
    rooms = db.Column('No. of Rooms',db.String(3)) # (String type) No operations will be performed
    bathrooms = db.Column('No. of Bathrooms',db.String(3)) # (String type) No operations will be performed
    price = db.Column('Price',db.String(12)) # (String type) No operations will be performed
    property_type = db.Column('Property Type',db.String(9))
    location = db.Column('Location',db.String(80))
    photo_name = db.Column('Photo Name',db.String(80))

    def __init__(self, title, description, rooms, bathrooms, price, propertyType, location, photo_name):
        self.title = title
        self.description = description
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.price = price
        self.property_type = propertyType
        self.location = location
        self.photo_name = photo_name

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<Property %r>' % (self.title)
