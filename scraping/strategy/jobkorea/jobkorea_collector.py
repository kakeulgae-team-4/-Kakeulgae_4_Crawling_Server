from collector import Collector
from strategy.jobkorea.jobkorea_web_driver import JobkoreaWebDriver


class JobkoreaCollector(Collector):
    def __init__(self):
        self.driver = JobkoreaWebDriver()

    def find_posts(self):
        self.driver.execute()


if __name__ == '__main__':
    collector1 = JobkoreaCollector()
    collector1.find_posts()
