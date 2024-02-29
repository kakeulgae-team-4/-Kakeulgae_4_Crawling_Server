import csv
import time

from web_driver import WebDriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from job_korea_config import path_repository as xpath


def get_path(path: str, *args):
    if len(args) == 1:
        return xpath['row'][path].format(idx=str(args[0]))
    elif len(args) == 2:
        return xpath['row'][path].format(idx=str(args[0]), span_idx=str(args[1]))


class JobkoreaWebDriver(WebDriver):
    def __init__(self):
        super(JobkoreaWebDriver, self).__init__()

    def wait_button_and_click(self, by, element: str):
        button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, element)))
        button.click()
        return button.text

    def wait_and_click_xpath(self, path: str):
        button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, path)))
        button.click()
        return button.text

    def find_by_xpath(self, path: str):
        return self.driver.find_element(By.XPATH, path)

    def init_order_select(self):
        self.body.send_keys(Keys.END)
        time.sleep(2)
        # 특정 엘리먼트가 나타날 때까지 스크롤 다운
        try:
            self.wait_and_click_xpath(xpath['order_tab'])
            self.wait_and_click_xpath(xpath['order_tab_optional'])
            self.page_source = self.driver.page_source
        except Exception as e:
            print("특정 엘리먼트가 발견되지 않았습니다. 스크롤을 내리면서 기다리겠습니다.")

    def init_order_select2(self):
        self.body.send_keys(Keys.END)
        time.sleep(2)
        # 특정 엘리먼트가 나타날 때까지 스크롤 다운
        try:
            self.wait_and_click_xpath(xpath['num_of_list_btn'])
            self.wait_and_click_xpath(xpath['num_50_of_list_btn'])
            self.page_source = self.driver.page_source
        except Exception as e:
            print("특정 엘리먼트가 발견되지 않았습니다. 스크롤을 내리면서 기다리겠습니다.")

    def maincrawling(self):
        time.sleep(0.5)

        page_button_next_xpath_pattern = xpath['page_next_button_pattern']
        # 초기 페이지 버튼 번호
        page_button_number = 2
        page_next_button_number = 2

        while True:
            try:
                for row_idx in range(1, 51):  # tr[1]부터 tr[50]까지
                    try:
                        # tr[현재 행 + 1]이 화면에 보이지 않으면 스크롤을 내리고 기다린다.
                        self.wait_and_click_xpath(get_path('one', row_idx))

                        # company name
                        company_name = self.find_by_xpath(get_path('company_name', row_idx)).text

                        # post name
                        post_name = self.find_by_xpath(get_path('post_name', row_idx)).text

                        # url
                        url = self.find_by_xpath(get_path('url', row_idx)).get_attribute('href')

                        # span 요소 수만큼 반복
                        span_texts = []  # span 요소들을 저장할 리스트
                        span_index = 1
                        while True:
                            try:
                                span_element = self.find_by_xpath(get_path('tag', row_idx, span_index)).text
                                span_texts.append(span_element)  # 각 span 요소를 리스트에 추가
                                span_index += 1
                            except:
                                break

                        # work type
                        work_type = self.find_by_xpath(get_path('work_type', row_idx)).text

                        # created at
                        created_at = self.find_by_xpath(get_path('created_at', row_idx)).text

                        # deadline
                        deadline = self.find_by_xpath(get_path('deadline', row_idx)).text
                    except Exception as e:
                        print(f"텍스트 {row_idx}를 가져오는데 실패했습니다.")

                # 페이지 버튼 클릭
                page_button_xpath = xpath['page_button_pattern'].format(page_button_number)

                self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
                time.sleep(0.5)
                page_button = self.driver.find_element(By.XPATH, page_button_xpath)
                page_button.click()
                time.sleep(0.5)
                page_button_number += 1
                page_next_button_number += 1
                if page_button_number == 11:
                    page_button_number = 2
                if page_next_button_number == 11:
                    self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
                    time.sleep(0.5)
                    page_next_button = self.find_by_xpath(xpath['page_next_button'])
                    page_next_button.click()
                    page_next_button_number += 1
                if page_next_button_number > 11 and page_next_button_number % 10 == 1:
                    self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
                    time.sleep(0.5)
                    page_next_button = self.find_by_xpath(page_button_next_xpath_pattern.format(2))
                    page_next_button.click()
                    page_next_button_number += 1
            except Exception as e:
                print("페이지 버튼이 더 이상 없습니다.")
                break
