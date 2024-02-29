from selenium.webdriver.common.by import By

from strategy.collector import Collector
from strategy.jobkorea.jobkorea_web_driver import JobkoreaWebDriver
from strategy.jobkorea.job_korea_config import url_repository as url
from strategy.jobkorea.job_korea_config import path_repository as xpath


class JobkoreaCollector(Collector):
    def __init__(self):
        self.source_page = None
        self.driver = JobkoreaWebDriver()
        self.driver.open_url(url['base'])

        # 버튼 요소 선택
        self.driver.wait_and_click_xpath(xpath['major_button'])
        print()

        # 두 번째 버튼 요소 선택
        self.driver.wait_and_click_xpath(xpath['middle_button'])
        print()

        sub_title_idx = 229
        for idx in range(1, 20):
            mid_path = f'//*[@id="duty_step2_10031_ly"]/li[{idx}]/label/span/span'
            sub_title = self.driver.wait_button_and_click(By.XPATH, mid_path)
            sub_path = f'//*[@id="duty_step3_1000{sub_title_idx}_ly"]'
            self.driver.wait_button(By.XPATH, sub_path, sub_title)
            sub_title_idx += 1

    def set_source_page(self):
        self.source_page = self.driver.get_page_source()


if __name__ == '__main__':
    strategy = JobkoreaCollector()
