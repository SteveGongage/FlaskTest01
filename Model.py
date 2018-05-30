from flask import Flask
from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

ma = Marshmallow()
db = SQLAlchemy()

class Comment(db.Model):
    __tablename__ = 'comments'
    
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(250), nullable=False)
    creation_date = db.Column(
        db.TIMESTAMP, 
        server_default=db.func.current_timestamp(),
        nullable=False,
        )
    
    category_id = db.Column(
        db.Integer,
        db.ForeignKey('categories.id', ondelete='CASCADE'),
        nullable=False,
        )
    
    category = db.relationship(
        'Category', 
        backref=db.backref('comments', lazy='dynamic')
        )
        
class Category(db.Model):
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(
        db.String(150), 
        unique=True, 
        nullable=False
        )
    
    def __init__(self, name):
        self.name = name
        
    
class CategorySchema(ma.Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    
class CommentSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    category_id = fields.Integer(required=True)
    comment = fields.String(
        require=True, 
        validate=validate.Length(1)
        )
    creation_date = fields.DateTime()
    

    
        
    