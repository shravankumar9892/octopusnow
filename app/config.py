import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = 'iamgoingtowin'
    WTF_CSRF_ENABLED = True
