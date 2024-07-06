import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    CELERY_BROKER_URL = 'redis://localhost:6379/0' #os.environ['CELERY_BROKER_URL']
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0' #os.environ['CELERY_RESULT_BACKEND']

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'


class TestingConfig(Config):
    TESTING = True