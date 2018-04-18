from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://www.guokr.com/")
#print(html.read())
bs_obj = BeautifulSoup(html.read(), "lxml")

titles = bs_obj.findAll("a", {"data-gaevent": "home_recommend_asks:v1.1.1.1:ask"})
# print(titles.count())
for title in titles:
    print(title.get_text())
