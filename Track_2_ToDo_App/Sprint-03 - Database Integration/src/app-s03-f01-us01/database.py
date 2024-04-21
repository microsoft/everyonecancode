from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Boolean, func
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class Todo(db.Model):
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(100), nullable=False)

    def __str__(self):
        return self.name
