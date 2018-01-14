from flask import jsonify

from MinProd import app
from MinProd.server.controllers.data import DataController


class SecurityController():
    @staticmethod
    def auth_user(token):
        dc = DataController()
        user = dc.get_user_by_token(token)
        if not user or not user.verify_auth_token():
            return False
        return True

    @staticmethod
    def generate_auth_token(username, password):
        dc = DataController()
        user = dc.get_user_by_username(username)
        if not user or not user.verify_password(password):
            return jsonify({ 'Error': '401 UNAUTHORIZED'})
        #token = binascii.b2a_hex(os.urandom(32))
        token = user.generate_auth_token(dc)
        output = jsonify({
            'token': token,
            'links':[{
                'rel':'help.private',
                'href':'https://localhost/help/private'
            }]
        })
        return output

