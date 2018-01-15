from flask import jsonify

class BaseView():
    @staticmethod
    def display_basic(key, value):
        return jsonify({ str(key): str(value)})

    # TODO: display dollar or decimal value
