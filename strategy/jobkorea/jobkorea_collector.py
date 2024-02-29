from collector import Collector
from jobkorea.jobkorea_web_driver import WebDriver
from bs4 import BeautifulSoup

from job_korea_config import path_repository as xpath
from job_korea_config import url_repository as url


class JobkoreaCollector(Collector):

    def __init__(self):
        self.source_page = None
        self.driver = WebDriver(False, False)
        self.driver.open_url(url['base'])

        # 분류 선택
        self.driver.wait_button_and_click(xpath['category_major_button'])
        self.driver.wait_button_and_click(xpath['category_middle_button'])
        self.driver.wait_button_and_click(xpath['category_sub_button'])

        self.driver.job_get_sub_title()
        self.driver.init_order_select()
        self.driver.init_order_select2()
        self.driver.maincrawling()

    def find_posts(self, source_page: str):
        pass

    def find_next_page(self):
        self.set_source_page()
        soup = BeautifulSoup(self.source_page, 'html.parser')

    def set_source_page(self):
        self.source_page = self.driver.get_page_source()
