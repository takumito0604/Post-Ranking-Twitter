
import requests
from bs4 import BeautifulSoup as BS
import urllib



url='https://www.amazon.co.jp/gp/bestsellers/electronics'

amzn=requests.get(url)

soup=BS(amzn.text,"lxml")

amzn_rank=soup.findAll("div",class_='zg_itemRow')

length=len(amzn_rank)

for i in range(length):

    print(amzn_rank[i].text)
