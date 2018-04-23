# coding:utf8
import os
from urllib import quote_plus as urlquote


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'asdfgn#&%^$*@%SDFsdfasdfsf*&&'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_POOL_SIZE = 50


class LocalConfig(Config):
    DEBUG = True
    db_name = "crawl"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'SQLALCHEMY_DATABASE_URI') or 'mysql://crawl:{}@127.0.0.1:3306/{}'.format(urlquote("asf%5333yhe#e"), db_name)


class DevConfig(Config):
    db_name = "crawl"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'SQLALCHEMY_DATABASE_URI') or \
        'mysql://crawl:{0}@rdsmuenvmmfjjrao.mysql.rds.aliyuncs.com:3306/{1}'.format(
            urlquote("asf%5333yhe#e"),
            db_name)


db_config = {
    'local': LocalConfig,
    'dev': DevConfig,
}
