import import_django
from posting_service.models import *
from scraping.service.post_service import PostService
from datetime import datetime, timedelta, date



ps = PostService()
ps.remove_all()
