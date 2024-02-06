import pymysql
import json


with open('db_meta.json') as key_file:
    db_meta = json.load(key_file)

conn = pymysql.connect(host=db_meta['host'],
                       user=db_meta['user'],
                       port=db_meta['port'],
                       password=db_meta['password'],
                       database=db_meta['database'])
cur = conn.cursor()
if cur is not None:
    print('connection success')