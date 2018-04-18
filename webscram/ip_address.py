from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())


def get_links(article_url):
    html = urlopen("http://en.wikipedia.org"+article_url)
    bs_obj = BeautifulSoup(html)
    return bs_obj.find("div", {"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))


def get_history_ips(page_url):
    # 编辑历史页面的url
    page_url = page_url.replace("/wiki/", "")
    history_url = "http://en.wikipedia.org/w/index.php?title="+page_url+"&action=history"
    print("history url is "+history_url)
    html = urlopen(history_url)
    bs_obj = BeautifulSoup(html)
    ip_addresses = bs_obj.findAll("a", {"class":"mw_anonuserlink"})
    address_list = set()
    for ip_address in ip_addresses:
        address_list.add(ip_address.get_text())
    return address_list


links = get_links("/wiki/Python_(programming_language)")
while(len(links)>0):
    for link in links:
        print("--------------------------")
        history_ips = get_history_ips(link.attrs['href'])
        for history_ip in history_ips:
            print(history_ip)

    new_link = links[random.randint(0, len(links) - 1)].attrs['href']
    links = get_links(new_link)