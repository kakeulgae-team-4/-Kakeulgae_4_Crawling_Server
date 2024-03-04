from typing import List
from domain.post.post import Post
from datetime import datetime, timedelta
import re


class IncruitPreprocessor:
    def batch_process(self, posts: List[Post]):
        for post in posts:
            self.education(post)

    def career(self, post: Post):
        post.career = post.career.replace('이상', '')
        post.career = post.career.replace('↑', '')
        careers = post.career.split('/')
        for career in careers:
            post.career = career

    def education(self, post: Post):
        post.education = post.education.replace('이상', '').strip()  # 대졸 이상 -> 대졸
        post.education = post.education.replace('↑', '').strip()  # 대졸↑ -> 대졸

    def deadline(self, post: Post):
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

    def created_at(self, post: Post):
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
