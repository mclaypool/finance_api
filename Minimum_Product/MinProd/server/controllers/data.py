from flask import jsonify
from sqlalchemy import create_engine, update
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import reflection

from MinProd import app
from MinProd.server.models.user import User


class DataController:
    def __init__(self):
        #set up sqlalchemy
        self.engine = create_engine(
            app.config['MINPRODDB']['conn'], 
            echo=False)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.session._model_changes = {}


    #SqlAlchemy functions
    def get_typesof_columns(self, table):
        insp = reflection.Inspector.from_engine(self.engine)
        return insp.get_columns(table)

    def get_first(self, table):
        return self.session.query(table).first()

    def get_all(self, table):
        return self.session.query(table).all()

    def get_user_by_username(self, username):
        return self.session.query(User).filter_by(Username=username).first()
  
    def get_user_by_token(self, token):
        try:
            return self.session.query(User).filter_by(Token=token).first()
        except:
            return None

    def add_user(self, user):
        self.session.add(user)
        self.session.commit()
    '''
    def update_user(self, user):
        #self.session.add(user)
        self.session.commit()
    '''
    def new_user(self, username, password):   
        if username is None or password is None: 
            abort(400) # missing arguments
        if self.get_user_by_username(username) is not None:
            abort(400) # existing user

        user = User(Username=username)
        user.hash_password(password)
        self.add_user(user)
        return jsonify({ 'username': user.Username })
