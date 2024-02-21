from bs4 import BeautifulSoup
from collector.Collector import Collector
from WebDriver import WebDriver
from domain.post.PostBuilder import PostBuilder
from collections import defaultdict
import json

from logger.stream_logger import StreamLogger
from logger.file_logger import FileLogger
from ParamPrinter import ParamPrinter


log = FileLogger()


class IncruitCollector(Collector):
    def __init__(self):
        self.posts = []
        self.base_url = None  # base url은 고정됨 -> config에서 불러옴
        self.url = None  # url은 page마다 변경됨 query parameter 수정해야함
        self.params = defaultdict(str)  # page는 변경되고 나머지는 고정
        self.webdriver = WebDriver()  # webdriver는 열려있음
        self.source_page = None  # source page는 변경됨
        self.init_params()

    def init_params(self):
        with open("incruit_config.json") as config_file:
            configs = json.load(config_file)
            self.base_url = configs['base_url']
            for key, value in configs.items():
                if not key.startswith('url') and not key.endswith('url'):
                    self.params[key] = value
            self.make_query_parameter()
        self.set_source_page()

    def make_query_parameter(self):
        param_list = []
        for key, value in self.params.items():
            param_list.append(key + '=' + self.params[key])
        self.url = self.base_url + '&'.join(param_list)

    def save_all_posts(self):
        while int(self.params['page']) <= 2:
            log.log(self.url)
            self.set_source_page()
            self.find_posts()
            for post in self.posts:
                ParamPrinter.log_class_param(log, post, self.params['page'])
            self.posts = []
            self.find_next_page()

    def next_page_exists(self):
        soup = BeautifulSoup(self.source_page, 'html.parser')
        next_button = soup.find('a', {'class': 'next_n'})
        if next_button:
            return True
        return False

    def find_posts(self, **kwargs):
        builder = PostBuilder()
        tags = []
        soup = BeautifulSoup(self.source_page, 'html.parser')
        content_list = soup.find('div', {'class': 'cBbslist_contenst'})
        contents = content_list.find_all('ul', {'class': 'c_row'})

        for content in contents:
            cell_first = content.find('div', {'class': 'cell_first'})
            cell_mid = content.find('div', {'class': 'cell_mid'})
            cell_last = content.find('div', {'class': 'cell_last'})

            company_name = cell_first.find('a', {'class': 'cpname'}).text  # 1. 회사이름
            post = cell_mid.find('div', {'class': 'cl_top'}).find('a')
            company_url = post.get('href')  # 회사 url
            post_name = post.text  # 2. 공고명
            url = post.get('href')  # 7. 공고 url

            spec = cell_mid.find('div', {'class': 'cl_md'}).find_all('span')
            career = spec[0].text  # 3. 경력
            education = spec[1].text  # 4. 교육
            location = spec[2].text  # 5. 지역
            job_type = spec[3].text  # 6. 채용 형태

            company_tags = cell_mid.find('div', {'class': 'cl_btm'}).find_all('span')

            for tag in company_tags:
                tags.append(tag.text)  # tag 정보

            dates = cell_last.find_all('span')  # 7. 마감
            deadline = dates[0].text
            created_at = dates[1].text

            self.add_post(builder, career, company_name, created_at, deadline, education, job_type, location, post_name,
                          url)

    def add_post(self, builder, career, company_name, created_at,
                 deadline, education, job_type, location, post_name, url):
        post_item = (builder.
                     company_name(company_name).
                     post_name(post_name).
                     career(career).
                     education(education).
                     location(location).
                     work_type(job_type).
                     url(url).
                     deadline(deadline).
                     created_at(created_at).
                     build())
        self.posts.append(post_item)

    def find_next_page(self):
        self.params['page'] = str(int(self.params['page']) + 1)
        self.make_query_parameter()

    def set_source_page(self):
        self.webdriver.open_url(self.url)
        self.source_page = self.webdriver.get_page_source()


if __name__ == '__main__':
    strategy = IncruitCollector()
    strategy.save_all_posts()
