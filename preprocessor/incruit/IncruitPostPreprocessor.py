from domain.post.Post import Post
from collections import deque
from datetime import datetime, timedelta
from copy import deepcopy
import re

from ParamPrinter import ParamPrinter


class IncruitPostPreprocessor:
    def __init__(self, post: Post):
        self.posts = deque()
        self.posts.append(post)
        self.res = []

    def process(self):
        self.career()
        self.education()
        self.deadline()
        self.created_at()
        for post in self.posts:
            ParamPrinter.print_class_params(post)
        items = []
        for post in self.posts:
            items.append(post)
        return items

    def career(self):
        for i in range(len(self.posts)):
            post = self.posts.popleft()

            post.career = post.career.replace('이상', '')
            post.career = post.career.replace('↑', '')
            careers = post.career.split('/')
            for career in careers:
                post.career = career
                self.posts.append(deepcopy(post))  # 신입/경력 -> ['신입', '경력']

    def education(self):
        for i in range(len(self.posts)):
            post = self.posts.popleft()
            post.education = post.education.replace('이상', '').strip()  # 대졸 이상 -> 대졸
            post.education = post.education.replace('↑', '').strip()  # 대졸↑ -> 대졸
            post.education = post.education.replace('학력', '').strip()  # 학력무관 -> 무관
            self.posts.append(post)

    def deadline(self):
        for i in range(len(self.posts)):
            post = self.posts.popleft()
            if post.deadline in ('상시', '채용시'):
                # 상시 또는 채용시 공고
                post.deadline = None
            elif post.deadline.startswith('~'):
                # ~02.04
                post.deadline = post.deadline[1:6].replace('.', '-')
                current_year = datetime.now().year
                date = f'{current_year}-{post.deadline}'
                formatted_date = datetime.strptime(date, '%Y-%m-%d')
                post.deadline = formatted_date.date().strftime("%Y-%m-%d")
            self.posts.append(post)

    def created_at(self):
        for i in range(len(self.posts)):
            post = self.posts.popleft()
            create_date = datetime.now().date()
            if '시간' in post.created_at:
                # n시간 전 공고
                """
                n시간 전이 하루 전이라면 날짜를 변경해주어야 함
                문자열 -> 날짜
                """
                post.created_at = create_date
            elif '일전' in post.created_at:
                # n일 전 공고
                posted_date = re.findall(r'\d+', post.created_at)
                print(type(create_date))
                post.created_at = create_date - timedelta(days=int(posted_date[0]))
            self.posts.append(post)
