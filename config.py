#！/usr/bin/env python
#-*- coding utf8 -*-

#！/usr/bin/env python
#-*- coding utf8 -*-
#配置文件
import os
basedir = os.path.abspath(os.path.dirname(__name__))

class Config(object):
    SECRET_KEY='123456'
    SQLALACHEMY_COMMIT_ON_TEARDOWN = True
    #FLASKY_MAIL_SUBJECT_PREFIX='[Flaky]'
    #FLASKY_MAIL_SENDER = 'Flasky Admin<flasky@example.com>'
    #FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    #MAIL_SERVER = 'smtp.qq.com'
    #MAIL_PORT = 567
    #MAIL_USE_TLS = True
    #MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLALACHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'dev_DB.db')
    DBPATH = os.path.join(basedir, 'dev_DB.db')

class TestingConfig(Config):
    TESTING = True
    SQLALACHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'test_DB.db')
    DBPATH = os.path.join(basedir, 'test_DB.db')

class ProductionConfig(Config):
    SQLALACHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.db')
    DBPATH = os.path.join(basedir, 'data.db')

config={
    'development':DevelopmentConfig,
    'test':TestingConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig
}
