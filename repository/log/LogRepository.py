from logger.file_logger import FileLogger


class LogRepository:
    log = FileLogger()
    path = '/Users/koo/PycharmProjects/scraping_server/logger/incruit/log.txt'

    @staticmethod
    def save(message: str):
        LogRepository.log.log(message)

    @staticmethod
    def get_last_log():
        with open(LogRepository.path, 'r') as log_file:
            logs = log_file.readlines()
        return logs[-1].split('|')[-1]
