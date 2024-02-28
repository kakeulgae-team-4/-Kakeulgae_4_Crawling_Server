from scheduler.scheduler import Scheduler
import logging
from time import time


def f1(logger, start_time):
    logger.info('function 1, interval = 3')
    logger.info(f'Time is {time() - start_time}')


def f2(logger, start_time):
    logger.info('function 2, interval = 5')
    logger.info(f'Time is {time() - start_time}')


if __name__ == '__main__':
    logger = logging.getLogger(name='Scheduler')
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('|%(asctime)s|%(name)s|%(levelname)s|%(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    start = time()
    scheduler = Scheduler()
    scheduler.add_job_with_seconds(3, f1, logger, start)
    scheduler.add_job_with_seconds(5, f2, logger, start)
    scheduler.run()
