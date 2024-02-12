from collector.Collector import Collector
from WebDriver import WebDriver
from bs4 import BeautifulSoup


class JobkoreaCollector(Collector):
    def __init__(self):
        self.source_page = None
        url = "https://www.jobkorea.co.kr/recruit/joblist?menucode=local&localorder=1#anchorGICnt_1"
        self.driver = WebDriver(False, False)
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

    def find_posts(self, source_page: str):
        pass

    def find_next_page(self):
        pass

    def set_source_page(self):
        self.source_page = self.driver.page_source()


if __name__ == '__main__':
    strategy = JobkoreaCollector()
