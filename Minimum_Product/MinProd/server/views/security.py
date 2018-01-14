from flask import jsonify


class SecurityView():
    @staticmethod
    def display_token_json(token):
        output = jsonify({
            'token': token,
            'links':[{
                'rel':'help.private',
                'href':'https://localhost/help/private'
            }]
        })

        return output
