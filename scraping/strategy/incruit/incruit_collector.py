from bs4 import BeautifulSoup
from strategy.collector import Collector
from web_driver import WebDriver
from dto.post.before_dto_builder import PostBuilder
from collections import defaultdict
from strategy.incruit.incruit_config import parameter_config as config
from strategy.incruit.incruit_preprocessor import IncruitPreprocessor


class IncruitCollector(Collector):
    def __init__(self):
        self.posts = []
        self.base_url = None  # base url은 고정됨 -> config에서 불러옴
        self.url = None  # url은 page마다 변경됨 query parameter 수정해야함
        self.params = defaultdict(str)  # page는 변경되고 나머지는 고정
        self.webdriver = WebDriver()  # webdriver는 열려있음
        self.preprocessor = IncruitPreprocessor()
        self.source_page = None  # source page는 변경됨
        self.init_params()
        self.builder = PostBuilder()

    def init_params(self):
        self.base_url = config['base_url']
        for key, value in config.items():
            if 'url' not in key:
                self.params[key] = value
        self.make_query_parameter()
        self.set_source_page()

    def make_query_parameter(self):
        param_list = []
        for key, value in self.params.items():
            param_list.append(key + '=' + self.params[key])
        self.url = self.base_url + '&'.join(param_list)

    def next_page_exists(self):
        soup = BeautifulSoup(self.source_page, 'html.parser')
        next_button = soup.find('a', {'class': 'next_n'})
        if next_button:
            return True
        return False

    def find_posts(self, **kwargs):
        while self.next_page_exists():
            self.set_source_page()
            self.find_one_page()
            self.preprocessor.batch_process(self.posts)
            self.posts = []
            self.find_next_page()

    def find_one_page(self):
        soup = BeautifulSoup(self.source_page, 'html.parser')
        content_list = soup.find('div', {'class': 'cBbslist_contenst'})
        contents = content_list.find_all('ul', {'class': 'c_row'})
        for content in contents:
            self.find_one(content)

    def find_one(self, content):
        cell_first = content.find('div', {'class': 'cell_first'})
        cell_mid = content.find('div', {'class': 'cell_mid'})
        cell_last = content.find('div', {'class': 'cell_last'})
        company_name = cell_first.find('a', {'class': 'cpname'}).text  # 회사 이름
        post = cell_mid.find('div', {'class': 'cl_top'}).find('a')
        post_name = post.text  # 공고명
        url = post.get('href')  # url
        spec = cell_mid.find('div', {'class': 'cl_md'}).find_all('span')
        career = spec[0].text
        education = spec[1].text
        location = spec[2].text
        work_type = spec[3].text
        company_tags = cell_mid.find('div', {'class': 'cl_btm'}).find_all('span')
        tags = []
        for tag in company_tags:
            tags.append(tag.text)
        dates = cell_last.find_all('span')
        deadline = dates[0].text
        created_at = dates[1].text

        post_dto = (self.builder.
                    company_name(company_name).
                    post_name(post_name).
                    career(career).
                    education(education).
                    location(location).
                    work_type(work_type).
                    job_detail(tags).
                    url(url).
                    deadline(deadline).
                    created_at(created_at).
                    build())
        self.posts.append(post_dto)

    def find_next_page(self):
        self.params['page'] = str(int(self.params['page']) + 1)
        self.make_query_parameter()

    def set_source_page(self):
        self.webdriver.open_url(self.url)
        self.source_page = self.webdriver.get_page_source()
