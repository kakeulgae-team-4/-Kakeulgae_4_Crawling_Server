<<<<<<< HEAD
# from bs4 import BeautifulSoup
#
# from PostBuilder import PostBuilder
# from Strategy import Strategy
#
#
# class JobkoreaStrategy(Strategy):
#     '''
#     * 수정
#         * 5분전수정
#         * 13분전 수정
#         * 점프업
#     * 등록
#         * 1시간 전 등록
#         * 21시간 전 등록
#         * 2일전 등록
#     '''
#     def execute(self, source_page: str):
#         print('jobkorea')
#         builder = PostBuilder()
#         tags = []
#         soup = BeautifulSoup(source_page, 'html.parser')
#         content_list = soup.find('div', {'class': 'tplList tplJobList'})
#         contents = content_list.find_all('tr', {'class': 'devlooopArea'})
#
#         for content in contents:
#             company_name = content.find('tr', {'class': 'tplCo'})
#
#             tplTit = content.find('td', {'class': })
# '''
# <div class="tplList tplJobList">
#     <tr class="devloopArea"> # row 하나 - o
#         <td class="tplCo"> # 기업명 - o
#         <td class="tplTit">
#             <a class="link normalLog"> # 공고명 - o
#             <p class="etc">
#                 **** cell ****
#                 cell 개수가 유동적
#                 -> 경력, 학력, 지역
#                 <span class="cell"> 경력무관 - o
#                 <span class="cell"> 학력무관 - o
#                     - upper arrow 처리
#                 <span class="cell"> 서울 강남구 - o
#                     - 울산울주군외 : 외 처리
#                 <span class="cell"> 정규직 - ox
#                     - 외 처리
#                 <span class="cell"> 10,000,000원(건)
#                 <span class="cell"> 팀원 - ox
#             <p class="dsc"> 수술, 성형외과, 수술실보조, 피부과, 성형, 수술실, 성형외과, 수술방
#         <td class="odd">
#             <span class="time dotum"> # 7분전 등록
#             <span class="date dotum"> # 마감일
#
# ex1.
# 경력, 학력, 지역, 채용유형
#
# ex2.
# 경력, 학력, 지역, 채용유형, 연봉, 직급
#
# ex3.
# 경력, 지역
# '''
# #
# # # Find all job listings
# # job_list_container = soup.find('div', class_='tplList tplJobList')
# #
# # # print(job_listings)
# #
# # jobs = []
# # if job_list_container:
# #     job_listings = job_list_container.find_all('tr', class_='devloopArea')
# #
# #     for job in job_listings:
# #         company = job.find('td', class_='tplCo')
# #         title = job.find('div', class_='titBx')
# #         details = job.find('p', class_='etc')
# #         description = job.find('p', class_='dsc')
# #
# #         # Check if 'title' attribute exists in 'a' tag within the title tag
# #         if title and title.find('a') and 'title' in title.find('a').attrs:
# #             company_name = company.find('a').text.strip() if company and company.find('a') else "N/A"
# #             job_title = title.find('a')['title'].strip()
# #
# #             if details:
# #                 detail_items = details.find_all('span', class_='cell')
# #                 requirements = [item.text.strip() for item in detail_items]
# #             else:
# #                 requirements = []
# #
# #             job_description = description.text.strip() if description else "N/A"
# #
# #             # Add to jobs list
# #             jobs.append({
# #                 'Company Name': company_name,
# #                 'Job Title': job_title,
# #                 'Requirements': requirements,
# #                 'Description': job_description
# #             })
# #
# # # Print the parsed data
# # for job in jobs:
# #     print(f"Company: {job['Company Name']}")
# #     print(f"Title: {job['Job Title']}")
# #     print(f"Requirements: {', '.join(job['Requirements'])}")
# #     print(f"Description: {job['Description']}\n\n")
=======
from collector.Collector import Collector
from WebDriver import WebDriver
from bs4 import BeautifulSoup


class JobkoreaCollector(Collector):
    def __init__(self):
        self.source_page = None
        url = "https://www.jobkorea.co.kr/recruit/joblist?menucode=local&localorder=1#anchorGICnt_1"
        self.driver = WebDriver(False, False)
        # self.driver = WebDriver()
        self.driver.open_url(url)

        # 버튼 요소 선택
        major_button_xpath = '/html/body/div[5]/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/dl[1]/dt/p'
        self.driver.wait_button_and_click(major_button_xpath)

        # 두 번째 버튼 요소 선택
        middle_button_xpath = '/html/body/div[5]/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/dl[1]/dd[2]/div[2]/dl[1]/dd/div[1]/ul/li[6]/label/span'
        self.driver.wait_button_and_click(middle_button_xpath)

        # 클릭
        sub_button_xpath = '/html/body/div[5]/div[1]/div/div[2]/div[1]/div[2]/div/div[1]/dl[1]/dd[2]/div[2]/dl[2]/dd/div[1]/ul[2]/li[1]/label/span'
        self.driver.wait_button_and_click(sub_button_xpath)

        self.driver.job_get_sub_title()
        self.driver.init_order_select()

    def find_posts(self, source_page: str):
        pass

    def find_next_page(self):
        self.set_source_page()
        soup = BeautifulSoup(self.source_page, 'html.parser')

    def set_source_page(self):
        self.source_page = self.driver.get_page_source()


if __name__ == '__main__':
    strategy = JobkoreaCollector()
    strategy.find_next_page()
>>>>>>> 205f0d7 (feat : job korea 동적 크롤링 코드 추가)
