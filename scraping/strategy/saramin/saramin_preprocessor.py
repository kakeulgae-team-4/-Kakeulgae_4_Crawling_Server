from typing import List
from dto.post.before_process_dto import BeforeProcessDto
from datetime import datetime, timedelta
import re

from post.after_process_dto import AfterProcessDto

"""
남은건 지역, 직무
지역은 DB연동해서 매핑 결과대로 전처리해준다. (지역1, 지역2로 나눠서 저장해야됨)
직무는 다른 사이트가 사람인 기준이니까 전처리를 해줄필요가 없나?
그런데 직무는 크롤링을 안해오고 있다..?익재는 태그1~태그6으로 크롤링했었음. 이게 dto에선 뭐에 해당하는건지 모르겠음.
"""

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

    def deadline(self, post: BeforeProcessDto):
        if '상시' in post.deadline or '채용시' in post.deadline:
            # 상시 또는 채용시 공고
            post.deadline = None
        elif post.deadline.startswith('D-'):
            # D-day 형식 처리
            days = int(post.deadline.split('-')[1])
            dday = datetime.now() - timedelta(days=days)
            post.deadline = dday.strftime("%Y-%m-%d")
        elif post.deadline.startswith('~'):
            # ~MM.DD(요일) 형식 처리
            date_str = post.deadline[1:].split('(')[0]  # 괄호와 요일 제거
            current_year = datetime.now().year
            date = f'{current_year}-{date_str.replace(".", "-")}'
            formatted_date = datetime.strptime(date, '%Y-%m-%d') #문자열을 datetime 객체로 변환
            post.deadline = formatted_date.strftime("%Y-%m-%d") #datetime 객체를 문자열로 다시 변환하여 저장

    def created_at(self, post: BeforeProcessDto):
        current_datetime = datetime.now()

        if '시간' in post.created_at:
            # n시간 전 공고
            hours = int(re.findall(r'\d+', post.created_at)[0])
            # n시간을 현재 시간에서 빼기
            posted_datetime = current_datetime - timedelta(hours=hours)
            # 게시된 날짜 설정
            post.created_at = posted_datetime.strftime("%Y-%m-%d")
        elif '일' in post.created_at:
            # n일 전 공고
            days_ago = int(re.findall(r'\d+', post.created_at)[0])
            # n일을 날짜로 변환
            posted_date = current_datetime - timedelta(days=days_ago)
            post.created_at = posted_date.strftime("%Y-%m-%d")


