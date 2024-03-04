from time import sleep

from selenium.common import NoSuchElementException

from web_driver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from jobkorea_config import path_repository as xpath
from jobkorea_config import *
from logger.file_logger import FileLogger

log = FileLogger()
log.setPath(param['log_path'])


class JobkoreaWebDriver(WebDriver):
    def __init__(self):
        super(JobkoreaWebDriver, self).__init__()
        self.page_button_num = 2
        self.page_next_button_num = 2

        self.open_url(url_repository['base'])
        self.job_get_sub_title()
        self.init_order_select(xpath['order_tab'], xpath['order_tab_optional'])
        self.init_order_select(xpath['num_of_list_btn'], xpath['num_50_of_list_btn'])

    def job_get_sub_title(self):
        self.driver.execute_script("window.scrollTo(0, 0);")
        self.wait_and_click_xpath(xpath['category_major_button'])
        self.wait_and_click_xpath(xpath['category_middle_button'])
        for i in range(1, param['sub_num']):
            self.wait_and_click_xpath(xpath['category_sub_button'].format(str(i)))
        self.wait_and_click_xpath(xpath['search_button'])

    def init_order_select(self, *args):
        sleep(param['short_time'])
        self.wait_and_click_xpath(args[0])
        self.wait_and_click_xpath(args[1])
        self.page_source = self.driver.page_source

    def execute(self):
        while True:
            try:
                for row_idx in range(1, param['row_num']):
                    self.find_one(row_idx)
                self.move_next_page()
            except Exception:
                print('Error occur')
                exit()
                pass

    def move_next_page(self):
        self.wait_and_click_xpath(xpath['page_button_pattern'].format(self.page_button_num))
        self.page_button_num += 1
        self.page_next_button_num += 1
        if self.page_button_num == 11:
            self.page_button_num = 2
        if self.page_next_button_num == 11:
            self.wait_and_click_xpath(xpath['page_next_button'])
        elif self.page_next_button_num > 11 and self.page_next_button_num % 10 == 1:
            self.wait_and_click_xpath(xpath['page_next_button_pattern'].format(2))
        self.page_next_button_num += 1

    def wait_and_click_xpath(self, path: str):
        button = (WebDriverWait(self.driver, 10).
                  until(ec.presence_of_element_located((By.XPATH, path))))
        print(button.text)
        button.click()

    def find_by_xpath(self, path: str):
        try:
            return self.driver.find_element(By.XPATH, path)
        except NoSuchElementException:
            return None

    def find_one(self, row_idx: int):
        company_name = self.find_by_xpath(get_row_path('company_name', row_idx)).text
        print('company_name', company_name)

        post_name = self.find_by_xpath(get_row_path('post_name', row_idx)).text
        print('post_name', post_name)

        url = self.find_by_xpath(get_row_path('url', row_idx)).get_attribute('href')
        print('url', url)

        job_detail_element = self.find_by_xpath(get_row_path('job_detail', row_idx))
        job_detail = job_detail_element.text if job_detail_element else None
        print('job_detail',  job_detail)

        created_at = self.find_by_xpath(get_row_path('created_at', row_idx)).text
        print('created_at', created_at)

        deadline = self.find_by_xpath(get_row_path('deadline', row_idx)).text
        print('deadline', deadline)

        tags_element = self.find_by_xpath(get_row_path('tags', row_idx))
        tags = tags_element.text.split() if tags_element else None
        print('tags', tags)
        print()


def get_row_path(path: str, row_idx: int):
    return xpath['row_base'].format(idx=row_idx) + xpath['row'][path]

