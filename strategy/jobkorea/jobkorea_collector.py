from collector import Collector
from strategy.jobkorea.jobkorea_web_driver import JobkoreaWebDriver
from bs4 import BeautifulSoup

from jobkorea_config import path_repository as xpath
from jobkorea_config import url_repository as url


class JobkoreaCollector(Collector):
    def __init__(self):
        self.driver = JobkoreaWebDriver()
        self.driver.execute()
