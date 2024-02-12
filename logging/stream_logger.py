import logging


class StreamLogger:
    logger = logging.getLogger(name='stream_logger')
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('|%(asctime)s||%(name)s||%(levelname)s|\n%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    @staticmethod
    def setLevel(level: str):
        if level == "CRITICAL":
            StreamLogger.logger.setLevel(logging.CRITICAL)
        if level == "FATAL":
            StreamLogger.logger.setLevel(logging.FATAL)
        if level == "ERROR":
            StreamLogger.logger.setLevel(logging.ERROR)
        if level == "WARNING":
            StreamLogger.logger.setLevel(logging.WARNING)
        if level == "WARN":
            StreamLogger.logger.setLevel(logging.WARN)
        if level == "INFO":
            StreamLogger.logger.setLevel(logging.INFO)
        if level == "DEBUG":
            StreamLogger.logger.setLevel(logging.DEBUG)
        if level == "NOTSET":
            StreamLogger.logger.setLevel(logging.NOTSET)

    @staticmethod
    def log(message: str):
        StreamLogger.logger.info(message)
