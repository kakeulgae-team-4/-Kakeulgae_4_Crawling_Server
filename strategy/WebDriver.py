import re
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


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

        # 여기에 User-Agent를 설정합니다. 사람인 IP차단 방지
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
        chrome_options.add_argument(f'user-agent={user_agent}')

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
