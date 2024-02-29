import csv
import time

from web_driver import WebDriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from job_korea_config import path_repository as xpath


class JobkoreaWebDriver(WebDriver):
    def __init__(self):
        super(JobkoreaWebDriver, self).__init__()

    def wait_button_and_click(self, by, element: str):
        button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, element)))
        button.click()
        return button.text

    def click_search_button(self):
        self.wait_button_and_click(By.ID, 'dev-btn-search')
        body = self.driver.find_element(By.TAG_NAME, 'body')
        print(body)

    def init_order_select(self):
        self.body.send_keys(Keys.END)
        time.sleep(2)
        # 특정 엘리먼트가 나타날 때까지 스크롤 다운
        try:
            self.wait_button_and_click(By.XPATH, xpath['order_tab'])
            self.wait_button_and_click(By.XPATH, xpath['order_tab_optional'])
            self.page_source = self.driver.page_source
        except Exception as e:
            print("특정 엘리먼트가 발견되지 않았습니다. 스크롤을 내리면서 기다리겠습니다.")

    def init_order_select2(self):
        self.body.send_keys(Keys.END)
        time.sleep(2)
        # 특정 엘리먼트가 나타날 때까지 스크롤 다운
        try:
            self.wait_button_and_click(xpath['num_of_list_btn'])
            self.wait_button_and_click(xpath['num_50_of_list_btn'])
            self.page_source = self.driver.page_source
        except Exception as e:
            print("특정 엘리먼트가 발견되지 않았습니다. 스크롤을 내리면서 기다리겠습니다.")

    def maincrawling(self):
        time.sleep(0.5)

        page_button_xpath_pattern = xpath['page_button_pattern']
        page_button_next_xpath_pattern = xpath['page_next_button_pattern']
        # 초기 페이지 버튼 번호
        page_button_number = 2
        page_next_button_number = 2

        while True:
            try:
                for tr_index in range(1, 51):  # tr[1]부터 tr[50]까지
                    try:
                        # tr[현재 행 + 1]이 화면에 보이지 않으면 스크롤을 내리고 기다린다.
                        WebDriverWait(self.driver, 10).until(
                            EC.presence_of_element_located((By.XPATH, xpath['row']['one'].format(idx=str(tr_index)))))

                        # company name
                        company_name = self.driver.find_element(By.XPATH, xpath['row']['company_name'].format(
                            idx=str(tr_index))).text

                        # post name
                        post_name = self.driver.find_element(By.XPATH,
                                                             xpath['row']['post_name'].format(idx=str(tr_index))).text

                        # url
                        url = self.driver.find_element(By.XPATH,
                                                       xpath['row']['url'].format(idx=str(tr_index))).get_attribute(
                            'href')

                        # span 요소 수만큼 반복
                        span_texts = []  # span 요소들을 저장할 리스트
                        span_index = 1
                        while True:
                            try:
                                span_element = self.driver.find_element(By.XPATH,
                                                                        xpath['row']['tag'].format(idx=str(tr_index)),
                                                                        span_idx=str(span_index))
                                span_text = span_element.text
                                span_texts.append(span_text)  # 각 span 요소를 리스트에 추가
                                print(f"태그 {span_index} : {span_text}")
                                span_index += 1
                            except:
                                # span 요소가 없으면 반복문 종료
                                break

                        # work type
                        work_type = self.driver.find_element(By.XPATH,
                                                             xpath['row']['work_type'].format(idx=str(tr_index))).text

                        # created at
                        created_at = self.driver.find_element(By.XPATH,
                                                              xpath['row']['created_at'].format(idx=str(tr_index))).text

                        # deadline
                        deadline = self.driver.find_element(By.XPATH,
                                                            xpath['row']['deadline'].format(idx=str(tr_index))).text
                    except Exception as e:
                        print(f"텍스트 {tr_index}를 가져오는데 실패했습니다.")

                # 페이지 버튼 클릭
                page_button_xpath = page_button_xpath_pattern.format(page_button_number)

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
                    page_next_button = self.driver.find_element(By.XPATH,
                                                                xpath['page_next_button'])
                    page_next_button.click()
                    page_next_button_number += 1
                if page_next_button_number > 11 and page_next_button_number % 10 == 1:
                    self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
                    time.sleep(0.5)
                    page_next_button = self.driver.find_element(By.XPATH, page_button_next_xpath_pattern.format(2))
                    page_next_button.click()
                    page_next_button_number += 1
            except Exception as e:
                print("페이지 버튼이 더 이상 없습니다.")
                break
