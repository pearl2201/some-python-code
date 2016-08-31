from app import db
from sqlalchemy import Column, Integer,String
class User(db.Model):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(64), index=True, unique=True)
    email = Column(String(120), index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % (self.nickname)