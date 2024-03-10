from typing import List
from dto.post.before_process_dto import BeforeProcessDto
from datetime import datetime, timedelta
import re

from post.after_process_dto import AfterProcessDto


class IncruitPreprocessor:
    def __init__(self):
        self.result: List[AfterProcessDto] = []

    def batch_process(self, posts: List[BeforeProcessDto]):
        for post in posts:
            self.education(post)
        self.result = []

    def education(self, post: BeforeProcessDto):
        post.education = post.education.replace('이상', '').strip()  # 대졸 이상 -> 대졸
        post.education = post.education.replace('↑', '').strip()  # 대졸↑ -> 대졸
        # if (post.education[:2] == '석사') or (post.education[:2] == '박사'):
        #     post.education += '졸업'

        # if '석사' in post.education:
        #     post.education = '석사졸업'

        # if '초대졸' in post.education:
        #     post.education = '대학졸업(2,3)년'

        # if '고졸' in post.education:
        #     post.education = '고등학교졸업'

    def deadline(self, post: BeforeProcessDto):
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

    def created_at(self, post: BeforeProcessDto):
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

    def career(self, post: BeforeProcessDto):
        if post.career[:2] == '신입':
            post.career = '신입'
        else:
            post.career = '경력'
