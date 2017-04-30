import logging
import os


DATABASE_URL = "127.0.0.1"
DATABASE_PORT = 27017


class BaseConfig(object):
    DEBUG = True
    TESTING = True
    SECRET_KEY = '1d94e52c-1c89-4515-b87a-f48cf3cb7f0b'
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = 'chrome-ext.log'
    LOGGING_LEVEL = logging.DEBUG


def configure_app(app):
    app.config.from_object(BaseConfig)
    # Configure logging
    handler = logging.FileHandler(app.config['LOGGING_LOCATION'])
    handler.setLevel(app.config['LOGGING_LEVEL'])
    formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
