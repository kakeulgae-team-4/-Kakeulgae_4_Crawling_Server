import csv

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from collector import Collector
from web_driver import WebDriver
from bs4 import BeautifulSoup
import time


class JobkoreaCollector(Collector):

    def __init__(self):
        self.source_page = None
        url = "https://www.jobkorea.co.kr/recruit/joblist?menucode=local&localorder=1#anchorGICnt_1"
        self.driver = WebDriver(False, False)
        # self.driver = WebDriver()
        self.driver.open_url(url)

        # 버튼 요소 선택
        major_button_xpath = '/html/body/div[5]/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/dl[1]/dt/p'
        self.driver.wait_button_and_click(major_button_xpath)

        # 두 번째 버튼 요소 선택
        middle_button_xpath = '/html/body/div[5]/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/dl[1]/dd[2]/div[2]/dl[1]/dd/div[1]/ul/li[6]/label/span'
        self.driver.wait_button_and_click(middle_button_xpath)

        # 클릭
        sub_button_xpath = '/html/body/div[5]/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/dl[1]/dd[2]/div[2]/dl[2]/dd/div[1]/ul[2]/li[1]/label/span'
        self.driver.wait_button_and_click(sub_button_xpath)

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
            xpath = '/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[2]/div[5]/div[2]/div[1]/select'
            optional_xpath = '/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[2]/div[5]/div[2]/div[1]/select/option[2]'
            self.wait_button_and_click(By.XPATH,  xpath)
            self.wait_button_and_click(By.XPATH, optional_xpath)
            self.page_source = self.driver.page_source
        except Exception as e:
            print("특정 엘리먼트가 발견되지 않았습니다. 스크롤을 내리면서 기다리겠습니다.")

    def init_order_select2(self):
        self.body.send_keys(Keys.END)
        time.sleep(2)
        # 특정 엘리먼트가 나타날 때까지 스크롤 다운
        try:
            xpath2 = '/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[2]/div[5]/div[2]/div[2]/select'
            optional_xpath2 = '/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[2]/div[5]/div[2]/div[2]/select/option[5]'
            self.wait_button_and_click(xpath2)
            self.wait_button_and_click(optional_xpath2)
            self.page_source = self.driver.page_source
        except Exception as e:
            print("특정 엘리먼트가 발견되지 않았습니다. 스크롤을 내리면서 기다리겠습니다.")

    def maincrawling(self):
        time.sleep(0.5)

        page_button_xpath_pattern = '/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[6]/div/ul/li[{}]/a'
        page_button_next_xpath_pattern = '/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[6]/div/p[{}]/a'
        # 초기 페이지 버튼 번호
        page_button_number = 2
        page_next_button_number = 2

        # CSV 파일 생성
        with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['회사이름', '회사설명', '회사URL', '태그1', '태그2', '태그3', '태그4', '태그5', '태그6', '두번째p요소직무', '첫번째span요소업로드시간', '두번째span요소마감시간']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            # 원하는 작업을 수행하고 나서 브라우저 닫기
            while True:
                try:
                    for tr_index in range(1, 51):  # tr[1]부터 tr[50]까지
                        try:
                            # tr[현재 행 + 1]이 화면에 보이지 않으면 스크롤을 내리고 기다린다.
                            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                                                 f'/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[5]/table/tbody/tr[{tr_index}]/td[2]/div/strong/a')))
                            a_element = self.driver.find_element(By.XPATH,
                                                                 f'/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[5]/table/tbody/tr[{tr_index}]/td[1]/a')
                            a_text = a_element.text
                            print(f"회사이름 {tr_index}: {a_text}")

                            text_element = self.driver.find_element(By.XPATH,
                                                                    f'/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[5]/table/tbody/tr[{tr_index}]/td[2]/div/strong/a')
                            text_value = text_element.text
                            print(f"회사설명{tr_index}: {text_value}")
                            # URL을 가져오기 위해 a 태그를 찾습니다.
                            url_element = self.driver.find_element(By.XPATH,
                                                                   f'/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[5]/table/tbody/tr[{tr_index}]/td[2]/div/strong/a')

                            # a 태그 내의 href 속성을 사용하여 URL을 가져옵니다.
                            url_value = url_element.get_attribute('href')

                            # 가져온 URL을 출력합니다.
                            print(f"회사 URL {tr_index}: {url_value}")

                            # span 요소 수만큼 반복
                            span_texts = []  # span 요소들을 저장할 리스트
                            span_index = 1
                            while True:
                                try:
                                    span_element = self.driver.find_element(By.XPATH,
                                                                            f'/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[5]/table/tbody/tr[{tr_index}]/td[2]/div/p[1]/span[{span_index}]')
                                    span_text = span_element.text
                                    span_texts.append(span_text)  # 각 span 요소를 리스트에 추가
                                    print(f"태그 {span_index} : {span_text}")
                                    span_index += 1
                                except:
                                    # span 요소가 없으면 반복문 종료
                                    break

                            # 두 번째 p 요소에 대한 처리
                            p2_element = self.driver.find_element(By.XPATH,
                                                                  f'/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[5]/table/tbody/tr[{tr_index}]/td[2]/div/p[2]')
                            p2_text = p2_element.text
                            print(f"두 번째 p 요소 직무 {tr_index}: {p2_text}")

                            # 첫 번째 span 요소에 대한 처리
                            span1_element = self.driver.find_element(By.XPATH,
                                                                     f'/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[5]/table/tbody/tr[{tr_index}]/td[4]/span[1]')
                            span1_text = span1_element.text
                            print(f"첫 번째 span 요소 업로드 시간 {tr_index}: {span1_text}")

                            # 두 번째 span 요소에 대한 처리
                            span2_element = self.driver.find_element(By.XPATH,
                                                                     f'/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[5]/table/tbody/tr[{tr_index}]/td[4]/span[2]')
                            span2_text = span2_element.text
                            print(f"두 번째 span 요소 마감 시간 {tr_index}: {span2_text}")

                            # CSV 파일에 데이터 작성
                            writer.writerow({
                                '회사이름': a_text,
                                '회사설명': text_value,
                                '회사URL': url_value,
                                '태그1': span_texts[0] if len(span_texts) > 0 else '',
                                '태그2': span_texts[1] if len(span_texts) > 1 else '',
                                '태그3': span_texts[2] if len(span_texts) > 2 else '',
                                '태그4': span_texts[3] if len(span_texts) > 3 else '',
                                '태그5': span_texts[4] if len(span_texts) > 4 else '',
                                '태그6': span_texts[5] if len(span_texts) > 5 else '',
                                '두번째p요소직무': p2_text,
                                '첫번째span요소업로드시간': span1_text,
                                '두번째span요소마감시간': span2_text
                            })

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
                                                                    '/html/body/div[5]/div[1]/div/div[2]/div[4]/div/div[6]/div/p/a')
                        page_next_button.click()
                        page_next_button_number += 1
                    if (page_next_button_number > 11 and page_next_button_number % 10 == 1):
                        page_next_button_xpath = page_button_next_xpath_pattern.format(2)
                        print(page_next_button_xpath)
                        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
                        time.sleep(0.5)
                        page_next_button = self.driver.find_element(By.XPATH, page_next_button_xpath)
                        page_next_button.click()
                        page_next_button_number += 1
                except Exception as e:
                    print("페이지 버튼이 더 이상 없습니다.")
                    break



if __name__ == '__main__':
    strategy = JobkoreaCollector()
    strategy.find_next_page()
