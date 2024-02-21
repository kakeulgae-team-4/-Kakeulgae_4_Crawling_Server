from bs4 import BeautifulSoup
from collector.Collector import Collector
from WebDriver import WebDriver
from domain.post.PostBuilder import PostBuilder
from collections import defaultdict
import json

from logger.stream_logger import StreamLogger
from logger.file_logger import FileLogger
from ParamPrinter import ParamPrinter

log = StreamLogger()


class SaraminCollector(Collector):
    def __init__(self):
        # 초기화 메서드에서는 여러 변수를 초기화합니다.
        self.posts = [] #크롤링한 데이터를 저장할 리스트
        self.base_url = None #크롤링할 웹사이트의 기본 URL
        self.url = None #실제 크롤링에 사용될 전체 URL
        self.params = defaultdict(str) # URL의 쿼리 파라미터를 저장
        self.webdriver = WebDriver() #웹 페이지에 액세스하고 DOM을 조작하기 위한 WebDriver 인스턴스
        self.source_page = None #WebDriver를 통해 가져온 현재 페이지의 소스 코드를 저장
        self.init_params() #URL설정부분

    def init_params(self):
        with open("saramin_config.json") as config_file:
            configs = json.load(config_file)
            self.base_url = configs['base_url']
            self.params = {k: v for k, v in configs.items() if k != 'base_url'}
            self.make_query_parameter()
        self.set_source_page()

    def make_query_parameter(self):
        param_list = [f"{key}={value}" for key, value in self.params.items()]
        self.url = f"{self.base_url}?{'&'.join(param_list)}"

    def save_all_posts(self):
        while int(self.params['page']) <= 2:
            log.log(self.url)
            self.set_source_page()
            self.find_posts()
            for post in self.posts:
                ParamPrinter.log_class_param(log, post, self.params['page'])
            # self.posts = []
            self.find_next_page()

    #크롤링 break걸어주는 함수?
    def next_page_exists(self):
        soup = BeautifulSoup(self.source_page, 'html.parser')
        next_button = soup.find('a', {'class': 'BtnNext'})
        if next_button:
            return True
        return False

    def find_posts(self, **kwargs):
        soup = BeautifulSoup(self.source_page, 'html.parser')
        jobs = soup.find_all('div', {'class': 'list_item'})

        for job in jobs:
            if not job.find('div', {'class': 'box_item'}):
                # box_item이 없으면 다음 job으로 넘어감.
                continue

            builder = PostBuilder()  # PostBuilder 인스턴스 생성
            # company_name= job.find('div', {'class': 'col company_nm'}).find(class_='str_tit')
            company_name = job.find('div', {'class': 'col company_nm'}).find(class_='str_tit').text.strip()

            log.log(company_name)

            post_name = job.find('div', {'class': 'job_tit'}).a.text.strip()

            post_url = "https://www.saramin.co.kr" + job.find('div', {'class': 'job_tit'}).a['href']

            # 근무지 추출
            work_place = job.find('p', {'class': 'work_place'}).text.strip() if job.find('p', {
                'class': 'work_place'}) else ''

            # 경력 요건 및 채용 형태 추출
            career_and_job_type = job.find('p', {'class': 'career'}).text.strip() if job.find('p', {
                'class': 'career'}) else ''
            if "·" in career_and_job_type:
                career, job_type = career_and_job_type.rsplit("·", 1)
                career = career.strip()
                job_type = job_type.strip()
            else:
                career = career_and_job_type  # "·"가 없는 경우 전체 문자열을 career로 간주
                job_type = ""  # 기본값 설정

            # 학력 요건 추출
            education = job.find('p', {'class': 'education'}).text.strip() if job.find('p',
                                                                                       {'class': 'education'}) else ''

            # 공고 기한 및 생성날짜 추출
            support_info = job.find('div', {'class': 'support_info'})
            deadline = support_info.find('span', {'class': 'date'}).text.strip() if support_info.find('span', {
                'class': 'date'}) else ''
            created_at = support_info.find('span', {'class': 'deadlines'}).text.strip() if support_info.find('span', {
                'class': 'deadlines'}) else ''

            # builder를 사용하여 Post 객체 설정 및 생성
            post = builder.company_name(company_name).post_name(post_name).career(career).education(education).location(
                work_place).work_type(job_type).url(post_url).deadline(deadline).created_at(created_at).build()

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
    strategy = SaraminCollector()
    strategy.save_all_posts()
    for pp in strategy.posts:
        print(pp.post_name)