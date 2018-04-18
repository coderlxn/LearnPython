from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
import MySQLdb

random.seed(datetime.datetime.now())

db = MySQLdb.connect("localhost", "lxn", "Blue1989pawn821_", "Scraw")
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# 使用execute方法执行SQL语句
cursor.execute("select version()")

'''
CREATE TABLE pages (id BIGINT(7) NOT NULL AUTO_INCREMENT, 
title VARCHAR(200), content VARCHAR(10000), created TIMESTAMP 
DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (id));
'''


def store(title, content):
    cursor.execute("INSERT INTO pages (title, content) VALUES (\"%s\", \"%s\")", (title, content))
    cursor.connection.commit()


def get_links(article_url):
    html = urlopen("http://en.wikipedia.org"+article_url)
    bs_obj = BeautifulSoup(html)
    title = bs_obj.find("h1").get_text()
    content = bs_obj.find("div", {"id": "mw-content-text"}).find("p").get_text()
    store(title, content)
    return bs_obj.find("div", {"id": "bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))


links = get_links("/wiki/Kevin_Bacon")
try:
    while len(links) > 0:
        new_article = links[random.randint(0, len(links) - 1)].attrs['href']
        print(new_article)
        links = get_links(new_article)
finally:
    cursor.close()
    db.close()