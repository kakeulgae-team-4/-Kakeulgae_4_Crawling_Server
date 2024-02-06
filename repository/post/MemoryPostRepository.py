from typing import List

from repository.post.PostRepository import PostRepository
from domain.post.Post import Post
import csv


class MemoryPostRepository(PostRepository):
    idx = 0
    csv_path = "/Users/koo/Desktop/git/job-webset-crawling/src/resources/incruit/result.csv"

    @staticmethod
    def save(data: Post, **kwargs):
        with open(MemoryPostRepository.csv_path, 'a') as file:
            writer = csv.writer(file)
            writer.writerow([data.company_name, data.post_name,
                             data.career, data.education,
                             data.location, data.location,
                             data.job_type, data.deadline,
                             data.url, data.created_at])

    @staticmethod
    def save_posts(data: List[Post], **kwargs):
        for datum in data:
            MemoryPostRepository.save(datum)

    @staticmethod
    def get_announcement_by_id(announcement_id: int, **kwargs):
        return None
        # return MemoryPostRepository.store[announcement_id]
