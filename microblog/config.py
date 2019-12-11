import os
# from dotenv import load_dotenv

# basedir = os.path.abspath(os.path.dirname(__file__))
# load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-not-guess"
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get("MAIL_SERVER") or "smtp.qq.com"
    MAIL_PORT = int(os.environ.get("MAIL_PORT") or 465)
    MAIL_USE_TLS = os.environ.get("MAIL_USE_LTS") or True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME") or "2191212732@qq.com"
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD") or "ototdpvasnsleccg"
    ADMINS = ['anyetiangong@qq.com']
    MS_TRANSLATOR_KEY = os.environ.get("MS_TRANSLATOR_KEY") or "fad3c6f8269e41a2868c843c9e839a37"
    POSTS_PER_PAGE = 3
    LANGUAGES = ['en', 'zh']
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL') or "http://localhost:9200"