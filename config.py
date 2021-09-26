
import os


class Config:
    '''
    General configuration parent class

    '''
    

    SECRET_KEY ='hdgvgvdvdvhdjjsjsvhsvs' 
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:wairimu22@localhost/bloggsapp'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    

    
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN =True



    MAIL_SERVER = 'smpt.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS =True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI= os.environ.get("DATABASE_URL")
    




class DevConfig(Config):
    '''
    Development configuration child class

    '''
    
    DEBUG = True


config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    
}
    