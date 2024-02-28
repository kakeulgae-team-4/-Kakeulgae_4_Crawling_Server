from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

naming_convention = {
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(column_0_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s'
}

db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    # 회사명
    company_name = db.Column(db.String(20), nullable=False)
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
    created_date = db.Column(db.DateTime(), nullable=False)

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


class Career(db.Model):
    __tablename__ = 'career'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(90))
    post = db.relationship('Post', backref='career', lazy=True)


class Education(db.Model):
    __tablename__ = 'education'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(90))
    post = db.relationship('Post', backref='education', lazy=True)


class Job(db.Model):
    __tablename__ = 'job'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(25))
    job_detail = db.relationship('JobDetail', backref='job', lazy=True)


class JobCategory(db.Model):
    __tablename__ = 'job_category'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(25))
    job_detail = db.relationship('JobDetail', backref='job_category', lazy=True)


class JobDetail(db.Model):
    __tablename__ = 'job_detail'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(25))
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=True)
    job_category_id = db.Column(db.Integer, db.ForeignKey('job_category.id'), nullable=True)
    post = db.relationship('Post', backref='job_detail', lazy=True)


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
