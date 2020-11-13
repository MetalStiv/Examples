from app import create_app

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'SecretKeyqwerty12345!!'

class DevelopmentConfig(Config):
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = 'm121144169'
    MYSQL_DATABASE_DB = 'example'
    MYSQL_DATABASE_HOST = 'localhost'
    DEBUG = True

app = create_app(DevelopmentConfig)
app.run('0.0.0.0', '5060')