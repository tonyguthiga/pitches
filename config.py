import os 

class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or 'postgresql+psycopg2://moring:Access@localhost/post'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SECRET_KEY = '\xd49\xaaO\xd6\xed\xccJ\xf2\x84\xaaH\xe7NF\xd6=\x9dz\xc3\xc4\xc3\xf3\xc7'

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or 'postgresql+psycopg2://moring:Access@localhost/post'

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moring:Access@localhost/post'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}