from flask_app import create_app


with app.app_context():
    all_posts = Post.query.all()
    for post in all_posts:
        print(post)
