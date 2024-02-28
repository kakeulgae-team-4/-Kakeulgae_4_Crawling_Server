import re
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import csv
import time

class WebDriver:
    """
    페이지만 크롤링함
    파싱은 하지 않음
    """

    def __init__(self, headless: bool = False, no_sandbox: bool = True):
        self.body = None
        self.page_source = None
        chrome_options = Options()
        if headless:
            chrome_options.add_argument('--headless')
        if no_sandbox:
            chrome_options.add_argument('--no-sandbox')
        chrome_options.add_experimental_option('detach', True)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

        self.driver = webdriver.Chrome(options=chrome_options)
        handles = self.driver.window_handles
        for handle in handles:
            if handle != handles[0]:
                self.driver.switch_to.window(handle)
                self.driver.close()
        self.driver.switch_to.window(handles[0])

    def open_url(self, url: str):
        self.driver.get(url)
        self.page_source = self.driver.page_source

    def get_page_source(self):
        return self.page_source

    def save_page_source(self, path: str):
        with open(path, 'w') as file:
            for line in self.page_source:
                file.write(line)
        print('page source saved')

    def get_elements_by_xpath(self, xpath: str):
        return self.driver.find_elements(By.XPATH, xpath)

    def get_elements_by_class(self, _class: str):
        return self.driver.find_elements(By.CLASS_NAME, _class)

    def get_element_by_class(self, _class: str):
        return self.driver.find_element(By.CLASS_NAME, _class)

    def get_elements_by_name(self, _class: str):
        return self.driver.find_elements(By.NAME, _class)

    def get_element_by_name(self, _class: str):
        return self.driver.find_element(By.NAME, _class)

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

    def get_page_nums(self):
        pass

    def page_num_exists(self):
        pass

    def wait_button(self, by, element: str, sub_title: str):
        elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, element)))
        elems = elem.text.split('\n')
        with open('/jobkorea/job_korea_job.csv', 'a') as file:
            for elem in elems:
                sub_title = re.sub(r'\((\d{1,3},?\d{1,3})*\)', '', sub_title)
                elem = re.sub(r'\((\d{1,3},?\d{1,3})*\)', '', elem)
                file.write(sub_title + ',' + elem)
                file.write('\n')
