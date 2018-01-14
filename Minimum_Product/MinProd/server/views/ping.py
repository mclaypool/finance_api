from flask import jsonify


class PingView():
    @staticmethod
    def display_response_json():
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