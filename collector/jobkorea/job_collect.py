import time

from selenium.webdriver.common.by import By

from collector.Collector import Collector
from WebDriver import WebDriver
from bs4 import BeautifulSoup

url = "https://www.jobkorea.co.kr/recruit/joblist?menucode=local&localorder=1#anchorGICnt_1"
major_button_xpath = '/html/body/div[5]/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/dl[1]/dt/p'
middle_button_xpath = '/html/body/div[5]/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/dl[1]/dd[2]/div[2]/dl[1]/dd/div[1]/ul/li[6]/label/span'


class JobkoreaCollector(Collector):
    def __init__(self):
        self.source_page = None
        self.driver = WebDriver()
        self.driver.open_url(url)

        # 버튼 요소 선택
        self.driver.wait_button_and_click(By.XPATH, major_button_xpath)
        print()

        # 두 번째 버튼 요소 선택
        self.driver.wait_button_and_click(By.XPATH, middle_button_xpath)
        print()

        sub_title_idx = 229
        for idx in range(1, 20):
            mid_path = f'//*[@id="duty_step2_10031_ly"]/li[{idx}]/label/span/span'
            sub_title = self.driver.wait_button_and_click(By.XPATH, mid_path)
            sub_path = f'//*[@id="duty_step3_1000{sub_title_idx}_ly"]'
            self.driver.wait_button(By.XPATH, sub_path, sub_title)
            sub_title_idx += 1

    def __del__(self):
        # self.driver.driver.quit()
        pass

    def find_posts(self, source_page: str):
        pass

    def find_next_page(self):
        self.set_source_page()

    def set_source_page(self):
        self.source_page = self.driver.get_page_source()

    def get_sub_title(self):
        pass


if __name__ == '__main__':
    strategy = JobkoreaCollector()
