from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://36kr.com/")
# print(html)
bs_obj = BeautifulSoup(html.read(), "lxml")

titles = bs_obj.findAll("h3", {"data-stat-click": re.compile("latest.zhufeed.wenzhangbiaoti.*")})
# print(titles.count())
for title in titles:
    print(title.get_text())
