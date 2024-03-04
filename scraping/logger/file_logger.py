import logging


class FileLogger:
    logger = logging.getLogger(name='file_logger')
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s|%(name)s|%(levelname)s|%(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    @staticmethod
    def setLevel(level: str):
        if level == "CRITICAL":
            FileLogger.logger.setLevel(logging.CRITICAL)
        if level == "FATAL":
            FileLogger.logger.setLevel(logging.FATAL)
        if level == "ERROR":
            FileLogger.logger.setLevel(logging.ERROR)
        if level == "WARNING":
            FileLogger.logger.setLevel(logging.WARNING)
        if level == "WARN":
            FileLogger.logger.setLevel(logging.WARN)
        if level == "INFO":
            FileLogger.logger.setLevel(logging.INFO)
        if level == "DEBUG":
            FileLogger.logger.setLevel(logging.DEBUG)
        if level == "NOTSET":
            FileLogger.logger.setLevel(logging.NOTSET)

    @staticmethod
    def setPath(filePath: str = '/Users/koo/PycharmProjects/scraping_server/logger/incruit/log.txt'):
        file_handler = logging.FileHandler(filePath, mode='a', encoding='utf')
        file_handler.setFormatter(FileLogger.formatter)
        FileLogger.logger.addHandler(file_handler)

    @staticmethod
    def log(*args):
        FileLogger.logger.info('||'.join(args))


if __name__ == '__main__':
    logger = FileLogger()
    logger.setPath()
    logger.log('test log!')
