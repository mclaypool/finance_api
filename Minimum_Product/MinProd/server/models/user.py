from sqlalchemy import Column, Date, String, Integer, func
from sqlalchemy.ext.declarative import declarative_base
from passlib.hash import cta_pbkdf2_sha1
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer
    as Serializer, BadSignature, SignatureExpired)

from MinProd import app
#from MinProd.server.models.base import Base


Base = declarative_base()


class User(Base):
    __tablename__ = 'User'
    id            = Column(Integer, primary_key = True)
    Username      = Column(String(32))
    PasswordHash  = Column(String(128))
    Token         = Column(String(34))

    def hash_password(self, password):
        self.PasswordHash = cta_pbkdf2_sha1.encrypt(password)
    
    def verify_password(self, password):
        return cta_pbkdf2_sha1.verify(password, self.PasswordHash)
    
    def generate_auth_token(self, dal, expiration=1200):
        s = Serializer(app.config['SECRET_KEY'], expires_in = expiration)
        token = s.dumps({ 'id': self.id })
        self.Token = token
        dal.add_user(self)
        return token
    
    def verify_auth_token(self):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(self.Token)
        except SignatureExpired:
            return False # valid token, but expired
        except BadSignature:
            return False # invalid token
        return True


#table build query and main temp
'''
CREATE TABLE User(
    id INTEGER PRIMARY KEY
    ,Username VARCHAR(32) NOT NULL UNIQUE
    ,PasswordHash VARCHAR(128) NOT NULL
    ,Token CHAR(34) NULL
    ,TokenExp DATETIME NULL
);
'''
