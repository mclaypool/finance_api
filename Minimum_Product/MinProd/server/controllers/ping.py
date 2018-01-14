from flask import jsonify


class PingController():
    @staticmethod
    def get_ping_json():
        output = jsonify({
            'links':
            [{
                'rel':'help.public',
                'href':'http://localhost/help'
            },{
                'rel':'token',
                'href':'https://localhost/token'
            }]
        })
        return output
