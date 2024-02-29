from time import sleep
from web_driver import WebDriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from jobkorea_config import path_repository as xpath
from jobkorea_config import url_repository

short_time = .5
long_time = 2


class JobkoreaWebDriver(WebDriver):
    def __init__(self):
        super(JobkoreaWebDriver, self).__init__()
        self.page_button_number = 2
        self.page_next_button_number = 2
        self.open_url(url_repository['base'])
        self.job_get_sub_title()
        self.init_order_select('order_tab', 'order_tab_optional')
        self.init_order_select('num_of_list_btn', 'num_50_of_list_btn')

    def job_get_sub_title(self):
        self.driver.execute_script("window.scrollTo(0, 0);")
        self.wait_and_click_xpath(xpath['category_major_button'])
        self.wait_and_click_xpath(xpath['category_middle_button'])
        for i in range(1, 20):
            try:
                self.wait_and_click_xpath(self.find_by_xpath('category_button'))
            except Exception as e:
                print(f"버튼 클릭에 실패했습니다: {e}")

        self.wait_and_click_xpath(self.find_by_xpath('search_button'))
        self.body = self.find_by_xpath(xpath['body'])

    def init_order_select(self, *args):
        self.find_by_xpath('body').send_keys(Keys.END)
        sleep(long_time)
        self.wait_and_click_xpath(args[0])
        self.wait_and_click_xpath(args[1])
        self.page_source = self.driver.page_source

    def execute(self):
        sleep(short_time)

        while True:
            try:
                for row_idx in range(1, 51):
                    self.get_one_row(row_idx)
                self.move_next_page()
            except Exception as e:
                print("페이지 버튼이 더 이상 없습니다.")
                break

    def move_next_page(self):
        self.wait_and_click_xpath(xpath['page_button_pattern'].format(self.page_button_number))
        self.page_button_number += 1
        self.page_next_button_number += 1
        if self.page_button_number == 11:
            self.page_button_number = 2
        if self.page_next_button_number == 11:
            self.wait_and_click_xpath(xpath['page_next_button'])
        elif self.page_next_button_number > 11 and self.page_next_button_number % 10 == 1:
            self.wait_and_click_xpath(xpath['page_next_button_pattern'].format(2))
        self.page_next_button_number += 1

    def wait_and_click_xpath(self, path: str):
        button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, path)))
        button.click()
        return button.text

    def find_by_xpath(self, path: str):
        return self.driver.find_element(By.XPATH, path) or None

    def get_one_row(self, row_idx: int):
        company_name = self.find_by_xpath(get_path('company_name', row_idx)).text
        post_name = self.find_by_xpath(get_path('post_name', row_idx)).text
        url = self.find_by_xpath(get_path('url', row_idx)).get_attribute('href')
        work_type = self.find_by_xpath(get_path('work_type', row_idx)).text
        created_at = self.find_by_xpath(get_path('created_at', row_idx)).text
        deadline = self.find_by_xpath(get_path('deadline', row_idx)).text
        tags = []
        tag_idx = 1
        while True:
            tag = self.find_by_xpath(get_path('tag', row_idx, tag_idx)).text
            if tag:
                tags.append(tag)
                tag_idx += 1
            else:
                break


def get_path(path: str, *args):
    if len(args) == 1:
        return xpath['row'][path].format(idx=str(args[0]))
    elif len(args) == 2:
        return xpath['row'][path].format(idx=str(args[0]), span_idx=str(args[1]))
