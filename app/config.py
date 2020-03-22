import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    CLIENT_KEY = os.environ.get('CLIENT_KEY')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    APM_URL = 'http://127.0.0.1:8200'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
