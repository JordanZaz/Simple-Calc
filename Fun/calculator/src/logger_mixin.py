import structlog

class LoggerMixin:
    def __init__(self):
        self.logger = structlog.get_logger(__name__)

    def bind_logger(self, **kwargs):
        self.logger = self.logger.bind(**kwargs)
