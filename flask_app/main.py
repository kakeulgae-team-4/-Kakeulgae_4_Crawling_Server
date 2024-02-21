from datetime import datetime, timedelta

from flask_app import app, db
from flask_app.models import *

with app.app_context():
    post = Post(company_name="카카오클라우드스쿨",
                career=Career.query.filter_by(type='1~3년').first(),
                education=Education.query.filter_by(type='석사졸업').first(),
                job_detail=JobDetail.query.filter_by(type='웹개발').first(),
                work_type=WorkType.query.filter_by(type='정규직').first(),
                region_2nd=Region2nd.query.filter_by(type='성남시').first(),
                post_name="개발자채용",
                deadline=datetime.now() + timedelta(10),
                url='www.naver.com',
                created_date=datetime.now())
    db.session.add(post)
    db.session.commit()
