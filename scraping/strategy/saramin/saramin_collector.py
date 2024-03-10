from bs4 import BeautifulSoup

from saramin.saramin_web_driver import SaraminWebDriver
from strategy.collector import Collector
from dto.post.before_dto_builder import PostBuilder
from collections import defaultdict
from strategy.saramin.saramin_config import parameter_config as configs
from logger.stream_logger import StreamLogger
from param_printer import ParamPrinter

log = StreamLogger()


class SaraminCollector(Collector):
    def __init__(self):
        # 초기화 메서드에서는 여러 변수를 초기화합니다.
        self.posts = [] #크롤링한 데이터를 저장할 리스트
        self.base_url = None #크롤링할 웹사이트의 기본 URL
        self.url = None #실제 크롤링에 사용될 전체 URL
        self.params = defaultdict(str) # URL의 쿼리 파라미터를 저장
        self.webdriver = SaraminWebDriver() #웹 페이지에 액세스하고 DOM을 조작하기 위한 WebDriver 인스턴스
        self.source_page = None #WebDriver를 통해 가져온 현재 페이지의 소스 코드를 저장
        self.init_params() #URL설정부분

    def init_params(self):
        self.base_url = configs['base_url']
        self.params = {k: v for k, v in configs.items() if k != 'base_url'}
        self.make_query_parameter()
        self.set_source_page()

    def make_query_parameter(self):
        param_list = [f"{key}={value}" for key, value in self.params.items()]
        self.url = f"{self.base_url}?{'&'.join(param_list)}"
        print(self.url)

    def find_posts(self, **kwargs):
        while True:
            self.set_source_page()
            self.find_one_page()
            for post in self.posts:
                ParamPrinter.log_class_param(log, post, self.params['page'])
            self.posts = []
            self.find_next_page()

    def find_one_page(self):
        soup = BeautifulSoup(self.source_page, 'html.parser')
        jobs = soup.find_all('div', {'class': 'list_item'})
        for job in jobs:
            if not job.find('div', {'class': 'box_item'}):
                continue

            builder = PostBuilder()  # PostBuilder 인스턴스 생성
            company_name = job.find('div', {'class': 'col company_nm'}).find(class_='str_tit').text.strip()
            post_name = job.find('div', {'class': 'job_tit'}).a.text.strip()
            post_url = "https://www.saramin.co.kr" + job.find('div', {'class': 'job_tit'}).a['href']
            work_place = job.find('p', {'class': 'work_place'}).text.strip() if job.find('p', {
                'class': 'work_place'}) else ''
            career_and_work_type = job.find('p', {'class': 'career'}).text.strip() if job.find('p', {
                'class': 'career'}) else ''
            if "·" in career_and_work_type:
                career, work_type = career_and_work_type.rsplit("·", 1)
                career = career.strip()
                work_type = work_type.strip()
            else:
                career = career_and_work_type  # "·"가 없는 경우 전체 문자열을 career로 간주
                work_type = ""  # 기본값 설정
            education = job.find('p', {'class': 'education'}).text.strip() if job.find('p',
                                                                                       {'class': 'education'}) else ''
            support_info = job.find('div', {'class': 'support_info'})
            deadline = support_info.find('span', {'class': 'date'}).text.strip() if support_info.find('span', {
                'class': 'date'}) else ''
            created_at = support_info.find('span', {'class': 'deadlines'}).text.strip() if support_info.find('span', {
                'class': 'deadlines'}) else ''
            post = builder.company_name(company_name).post_name(post_name).career(career).education(education).location(
                work_place).work_type(work_type).url(post_url).deadline(deadline).created_at(created_at).build()

            self.posts.append(post)

    def find_next_page(self):
        self.params['page'] = str(int(self.params['page']) + 1)
        self.make_query_parameter()
        self.set_source_page()

    def set_source_page(self):
        # WebDriver를 사용해 현재 설정된 URL의 페이지를 로드하고 HTML 소스를 가져옴
        self.webdriver.open_url(self.url)
        self.source_page = self.webdriver.get_page_source()

if __name__ == '__main__':
    tmp = SaraminCollector()
    tmp.find_posts()
