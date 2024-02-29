from time import sleep
from web_driver import WebDriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from job_korea_config import path_repository as xpath


short_time = .5
long_time = 2


def get_path(path: str, *args):
    if len(args) == 1:
        return xpath['row'][path].format(idx=str(args[0]))
    elif len(args) == 2:
        return xpath['row'][path].format(idx=str(args[0]), span_idx=str(args[1]))


class JobkoreaWebDriver(WebDriver):
    def __init__(self):
        super(JobkoreaWebDriver, self).__init__()

    def wait_and_click_xpath(self, path: str):
        button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, path)))
        button.click()
        return button.text

    def find_by_xpath(self, path: str):
        return self.driver.find_element(By.XPATH, path) or None

    def init_order_select(self):
        self.find_by_xpath('body').send_keys(Keys.END)
        sleep(long_time)
        try:
            self.wait_and_click_xpath(xpath['order_tab'])
            self.wait_and_click_xpath(xpath['order_tab_optional'])
            self.page_source = self.driver.page_source
        except Exception as e:
            print("특정 엘리먼트가 발견되지 않았습니다. 스크롤을 내리면서 기다리겠습니다.")

    def init_order_select2(self):
        self.find_by_xpath('body').send_keys(Keys.END)
        sleep(long_time)
        try:
            self.wait_and_click_xpath(xpath['num_of_list_btn'])
            self.wait_and_click_xpath(xpath['num_50_of_list_btn'])
            self.page_source = self.driver.page_source
        except Exception as e:
            print("특정 엘리먼트가 발견되지 않았습니다. 스크롤을 내리면서 기다리겠습니다.")

    def execute(self):
        sleep(short_time)

        # 초기 페이지 버튼 번호
        page_button_number = 2
        page_next_button_number = 2

        while True:
            try:
                for row_idx in range(1, 51):  # tr[1]부터 tr[50]까지
                    self.wait_and_click_xpath(get_path('one', row_idx))
                    self.get_one_row(row_idx)

                page_button_next_xpath_pattern = xpath['page_next_button_pattern']
                self.wait_and_click_xpath(xpath['page_button_pattern'].format(page_button_number))
                page_button_number += 1
                page_next_button_number += 1
                if page_button_number == 11:
                    page_button_number = 2

                if page_next_button_number == 11:
                    page_next_button = self.find_by_xpath(xpath['page_next_button'])
                    page_next_button.click()
                elif page_next_button_number > 11 and page_next_button_number % 10 == 1:
                    page_next_button = self.find_by_xpath(page_button_next_xpath_pattern.format(2))
                    page_next_button.click()

                page_next_button_number += 1
            except Exception as e:
                print("페이지 버튼이 더 이상 없습니다.")
                break

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
