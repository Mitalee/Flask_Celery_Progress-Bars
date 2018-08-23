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
    CELERY_BROKER_URL = 'redis://h:p3faa7ba22573025735fd035250d343589dee577f09c62160de264c6ea4e2e5be@ec2-35-169-104-48.compute-1.amazonaws.com:16069'
    CELERY_RESULT_BACKEND = 'redis://h:p3faa7ba22573025735fd035250d343589dee577f09c62160de264c6ea4e2e5be@ec2-35-169-104-48.compute-1.amazonaws.com:16069'

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'


class TestingConfig(Config):
    TESTING = True