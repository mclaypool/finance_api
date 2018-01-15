from flask_sslify import SSLify
from subprocess import Popen

from MinProd import app


if app.config['DEBUG'] == True:
    app.run(debug=True)
else:
    sslify = SSLify(app)
    cmd = "gunicorn -b 0.0.0.0:80 -c %s MinProd:app" \
        % app.config['GUNICORN']
    Popen(cmd, shell=True).wait()
