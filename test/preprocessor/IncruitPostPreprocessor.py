from domain.post.PostBuilder import PostBuilder
from preprocessor.incruit.IncruitPostPreprocessor import IncruitPostPreprocessor
import unittest


class IncruitPreprocessorTest(unittest.TestCase):
    def setUp(self):
        self.builder = PostBuilder()
        self.item = (self.builder.company_name("충북개발공사").
                     post_name("2024년 정규직(신입/경력) 채용 공고").
                     career("신입/경력(연차무관)").
                     education("박사 이상").
                     location("충북 청주시").
                     work_type("정규직").
                     deadline("~02.08 (목)").
                     url("https://job.incruit.com/jobdb_info/jobpost.asp?job=2401290004100").
                     created_at("(3일전 등록)").build())
        self.preprocessor = IncruitPostPreprocessor(self.item)
        self.preprocessor.career()

    def test_career(self):
        self.assertEqual(len(self.preprocessor.posts), 2)
        self.assertEqual(self.preprocessor.posts[0].career, '신입')
        self.assertEqual(self.preprocessor.posts[1].career, '경력(연차무관)')

    def test_education(self):
        self.assertEqual(self.preprocessor)

if __name__ == '__main__':
    unittest.main()
