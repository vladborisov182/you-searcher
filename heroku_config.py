import logging
from logging import StreamHandler

from app import app
from config import Configuration


class HerokuConfig(Configuration):
    @classmethod
    def init_app(cls, app):
        ProductionConfig.init_app(app)
    
    file_handler = StreamHandler()
    file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)
