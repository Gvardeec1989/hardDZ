from setup_db import db

from marshmallow import Schema, fields


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()


class Director(db.Model):
    __tablname__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    def __str__(self):
        return self.name