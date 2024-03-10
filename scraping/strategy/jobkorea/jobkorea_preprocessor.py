import import_django

from typing import List
from dto.post.post import Post
from datetime import datetime, timedelta
import re

class JobkoreaPreprocessor:
    def batch_process(self, posts: List[Post]):
        for post in posts:
            self.education(post)
            self.deadline(post)
            self.created_at(post)
            self.career(post)
            # 필요한 경우 다른 전처리 메서드를 추가하여 호출할 수 있습니다.

    def education(self, post: Post):
        post.education = post.education.replace('이상', '').strip()  # 대졸 이상 -> 대졸
        post.education = post.education.replace('↑', '').strip()  # 대졸↑ -> 대졸
        if (post.education[:2] == '석사') or (post.education[:2] == '박사'):
            post.education += '졸업'

        # if '석사' in post.education:
        #     post.education = '석사졸업'

        # if '초대졸' in post.education:
        #     post.education = '대학졸업(2,3)년'

        # if '고졸' in post.education:
        #     post.education = '고등학교졸업'

    def deadline(self, post: Post):
        if post.deadline in ('상시', '채용시'):
            post.deadline = None
        elif post.deadline.startswith('~'):
            post.deadline = post.deadline[1:6].replace('.', '-')
            current_year = datetime.now().year
            date = f'{current_year}-{post.deadline}'
            formatted_date = datetime.strptime(date, '%Y-%m-%d')
            post.deadline = formatted_date.date().strftime("%Y-%m-%d")

    def created_at(self, post: Post):
        create_date = datetime.now().date()
        if '시간' in post.created_at:
            post.created_at = create_date
        elif '일전' in post.created_at:
            posted_date = re.findall(r'\d+', post.created_at)
            post.created_at = create_date - timedelta(days=int(posted_date[0]))

    def career(self, post: Post):
        # post.career = post.career.replace('이상', '')
        # post.career = post.career.replace('↑', '')
        # careers = post.career.split('/')
        # for career in careers:
        #     post.career = career.strip()

        # '경력무관'인 경우 '신입'과 '경력'으로 모두 처리
        if '경력무관' in post.career:
            post.career = ['신입', '경력']

        else:
            if '·' in post.career:
                careers = post.career.split('·')

                post.career = list(map(lambda x: x[:2], careers))
                # processed_careers = []
                # for career in careers:
                #     if '경력' in career:
                #         # 경력 뒤에 있는 모든 데이터 삭제
                #         career = '경력'
                #     processed_careers.append(career.strip())
                # post.career = processed_careers

            else:
                # 그 외의 경우에는 단순히 데이터의 앞뒤 공백을 제거
                post.career = post.career.strip()

        if post.career.startswith('경력'):
            post.career = '경력'

    def region(self, post: Post):
        # '구로구' 단어 발견 시 전처리
            if '구로구' in post.region:
                post.region = '구로구'
            else:
                # 그 외의 경우에는 기존 데이터 그대로 사용
                post.region = post.region.strip()

