from typing import List
from dto.post.before_process_dto import BeforeProcessDto
from datetime import datetime, timedelta
import re

from post.after_process_dto import AfterProcessDto


class SaraminPreprocessor:
    def __init__(self):
        self.result: List[AfterProcessDto] = []

    def batch_process(self, posts: List[BeforeProcessDto]):
        for post in posts:
            self.education(post)
        self.result = []

    def education(self, post: BeforeProcessDto):
        if '고졸' in post.education:
            post.education = '고졸'
        elif '3년' in post.education:
            post.education = '초대졸'
        elif '4년' in post.education:
            post.education = '대졸'
        elif '석사' in post.education:
            post.education = '석사'

    def career(self, post: BeforeProcessDto):
        if '신입 · 경력' in post.career or '무관' in post.career:
            post.career = ['신입', '경력']
        elif '년' in post.career:
            post.career = '경력'
        elif '신입' in post.career:
            post.career = '신입'



