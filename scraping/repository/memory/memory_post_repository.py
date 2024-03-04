from typing import List

from repository import Repository
from dto.post.post import Post
import csv


class MemoryRepository(Repository):
    idx = 0
    csv_path = "/Users/koo/Desktop/git/job-webset-crawling/src/resources/incruit/result.csv"
    log_path = "/Users/koo/PycharmProjects/scraping_server/logger/incruit/log.txt"

    @staticmethod
    def save(data: Post, **kwargs):
        with open(MemoryRepository.csv_path, 'a') as file:
            writer = csv.writer(file)
            writer.writerow([data.company_name, data.post_name,
                             data.career, data.education,
                             data.location, data.location,
                             data.work_type, data.deadline,
                             data.url, data.created_at])

    @staticmethod
    def save_posts(data: List[Post], **kwargs):
        for datum in data:
            MemoryRepository.save(datum)

    @staticmethod
    def find_one(announcement_id: int, **kwargs):
        return None
        # return MemoryPostRepository.store[announcement_id]
