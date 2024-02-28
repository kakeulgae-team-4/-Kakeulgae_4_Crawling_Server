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
