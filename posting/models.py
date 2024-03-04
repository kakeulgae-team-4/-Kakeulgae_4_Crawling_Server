from django.db import models


class Bookmark(db.Model):
    __tablename__ = 'bookmark'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    job_posting_id = db.Column(db.Integer, db.ForeignKey('job_posting.id', name='fk_bookmark_job_posting_id'))
    member_id = db.Column(db.Integer, db.ForeignKey('member.id', name='fk_bookmark_member_id'))


class Career(db.Model):
    __tablename__ = 'career'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(90))
    post = db.relationship('Post', backref='career', lazy=True)

    __table_args__ = (db.UniqueConstraint('type', name='career_uk'),
                      db.Index('career_idx_type', 'type'))


class Education(db.Model):
    __tablename__ = 'education'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(90))
    post = db.relationship('Post', backref='education', lazy=True)

    __table_args__ = (db.UniqueConstraint('type', name='education_uk'),
                      db.Index('education_idx_type', 'type'))


class Job(db.Model):
    __tablename__ = 'job'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(25))
    job_detail = db.relationship('JobDetail', backref='job', lazy=True)

    __table_args__ = (db.UniqueConstraint('type', name='job_uk'),
                      db.Index('job_idx_type', 'type'))


class JobCategory(db.Model):
    __tablename__ = 'job_category'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(90))
    job_detail = db.relationship('JobDetail', backref='job_category', lazy=True)

    __table_args = (db.UniqueConstraint('type', name='job_category_uk'),
                    db.Index('job_idx_type', 'type'))


class JobDetail(db.Model):
    __tablename__ = 'job_detail'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(255))
    job_id = db.Column(db.Integer, db.ForeignKey('job.id', name='job_fk'))
    job_category_id = db.Column(db.Integer, db.ForeignKey('job_category.id', name='job_category_fk'))
    post = db.relationship('Post', backref='job_detail', lazy=True)

    __table_args__ = (db.UniqueConstraint('type', 'job_id', name='job_detail_uk'),
                      db.Index('job_detail_idx_type', 'type'))


class JobPost(db.Model):
    __tablename__ = 'job_posting'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 회사명
    company_name = db.Column(db.String(90), nullable=False)
    # 공고명
    post_name = db.Column(db.String(255), nullable=False)
    # 경력명
    career_id = db.Column(db.Integer, db.ForeignKey('career.id'))
    # 교육수준명
    education_id = db.Column(db.Integer, db.ForeignKey('education.id'))
    # 채용분야명
    job_detail_id = db.Column(db.Integer, db.ForeignKey('job_detail.id'))
    # 지역명
    region_2nd_id = db.Column(db.Integer, db.ForeignKey('region_2nd.id'))
    # 채용형태명
    work_type_id = db.Column(db.Integer, db.ForeignKey('work_type.id'))
    deadline = db.Column(db.DateTime(), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)

    def __repr__(self):
        return (f'<Post {self.company_name}'
                f', {self.post_name}'
                f', {self.career}'
                f', {self.education}'
                f', {self.location}'
                f', {self.job_type}'
                f', {self.deadline}'
                f', {self.url}'
                f', {self.created_date}>')

class Region1st(db.Model):
    __tablename__ = 'region_1st'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(25))
    region2nd = db.relationship('Region2nd', backref='region1st', lazy=True)


class Region2nd(db.Model):
    __tablename__ = 'region_2nd'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(25))
    region1st_id = db.Column(db.Integer, db.ForeignKey('region_1st.id'), nullable=False)
    post = db.relationship('Post', backref='region_2nd', lazy=True)


class WorkType(db.Model):
    __tablename__ = 'work_type'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(25))
    post = db.relationship('Post', backref='work_type', lazy=True)
