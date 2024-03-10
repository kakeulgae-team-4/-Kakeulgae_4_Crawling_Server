import import_django

from typing import List
from datetime import datetime, timedelta
import re

from db_repository import JobkoreaRegionMappingRepository
from post.before_process_dto import BeforeProcessDto
from post.after_dto_builder import AfterDtoBuilder
from service.post_service import PostService


class JobkoreaPreprocessor:
    def __init__(self):
        self.region_mapping = JobkoreaRegionMappingRepository()
        self.builder = AfterDtoBuilder()

    def batch_process(self, posts: List[BeforeProcessDto]):
        for post in posts:
            (self.builder
             .company_name(post.company_name)
             .post_name(post.post_name)
             .url(post.url))

            self.education(post.education)
            self.deadline(post.deadline)
            self.created_at(post)
            self.career(post)
            new_post = self.builder.build()  # post 객체 하나 생성
            self.service.save_post(new_post)

            # 필요한 경우 다른 전처리 메서드를 추가하여 호출할 수 있습니다.

    def education(self, education: str):
        education = education.replace('이상', '').strip()  # 대졸 이상 -> 대졸
        education = education.replace('↑', '').strip()  # 대졸↑ -> 대졸
        if (education[:2] == '석사') or (education[:2] == '박사'):
            education += '졸업'
        self.builder.education(education)

        # if '석사' in post.education:
        #     post.education = '석사졸업'

        # if '초대졸' in post.education:
        #     post.education = '대학졸업(2,3)년'

        # if '고졸' in post.education:
        #     post.education = '고등학교졸업'

    def deadline(self, deadline: str):
        if deadline in ('상시', '채용시'):
            deadline = None
        elif deadline.startswith('~'):
            deadline = deadline[1:6].replace('.', '-')
            current_year = datetime.now().year
            date = f'{current_year}-{deadline}'
            formatted_date = datetime.strptime(date, '%Y-%m-%d')
            deadline = formatted_date.date().strftime("%Y-%m-%d")
        self.builder.deadline(deadline)

    def created_at(self, post: BeforeProcessDto):
        create_date = datetime.now().date()
        if '시간' in post.created_at:
            post.created_at = create_date
        elif '일전' in post.created_at:
            posted_date = re.findall(r'\d+', post.created_at)
            post.created_at = create_date - timedelta(days=int(posted_date[0]))

    def career(self, post: BeforeProcessDto):
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

    def region(self, region_info: str):

        # '서울 금천구 외'와 같은 데이터를 공백을 기준으로 분리하여 처리
        region_info = region_info[:2] if region_info[-2:] == ' 외' else region_info
        mapped_region_info = self.region_mapping.find_one(region_info)
        mapped_region_info.split()
        self.builder.region_1st(mapped_region_info[0])
        if len(mapped_region_info) >= 2:
            self.builder.region_2nd(mapped_region_info[1])
        else:
            pass

        # region_data = post.region.split()
        # if len(region_data) >= 2:
        #     post.first_region = region_data[0]
        #     post.second_region = region_data[1]
        # else:
        #     post.first_region = post.region.strip()
        #     post.second_region = None
        #
        # if '세종' in post.region:
        #     post.region = '세종특별자치시'
        #
        # if any(country in post.region for country in ['대만','말레이시아','몽골','미얀마',
        #     '방글라데시','베트남','사우디아라비아', '스리랑카','싱가포르','인도','인도네시아','일본','중국.홍콩','캄보디아',
        #     '태국','필리핀','네팔','라오스','아랍에미레이트연방','우즈베키스탄','이라크','카타르','파키스탄','멕시코',
        #     '캐나다','과테말라','브라질','페루','니카라과','네덜란드','독일','스웨덴','스위스','스페인','영국',
        #     '이탈리아','체코','터키','폴란드','프랑스','헝가리','루마니아','슬로바키아','오스트리아','괌','뉴질랜드',
        #     '호주','나이지리아','남아프리카공화국','모로코','이집트','말라위','모잠비크','세네갈','적도기니','보스턴',
        #     '뉴욕','로스엔젤레스','네바다주','뉴욕주','뉴저지주','로드아일랜드주','메릴랜드주','미시건주','앨라배마주',
        #     '오레건주','오하이오주','워싱턴주','인디애나주','일리노이주','조지아주','캘리포니아주','켄터키주',
        #     '테네시주','텍사스주']):
        #
        #     post.region = '해외'
