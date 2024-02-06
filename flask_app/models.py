from flask_app import db


class Post(db.Model):
    company_name = db.Column(db.String(20), primary_key=True)
    post_name = db.Column(db.String(255), primary_key=True)
    career = db.Column(db.String(20))
    education = db.Column(db.String(20))
    location = db.Column(db.String(20))
    job_type = db.Column(db.String(20))
    deadline = db.Column(db.DateTime(), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    created_date = db.Column(db.DateTime(), nullable=False)
