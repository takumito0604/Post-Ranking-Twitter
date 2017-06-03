#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from requests_oauthlib import OAuth1Session
from bs4 import BeautifulSoup as BS
import requests
import urllib



url='https://www.amazon.co.jp/gp/bestsellers/electronics'

amzn=requests.get(url)

soup=BS(amzn.text,"lxml")

amzn_rank=soup.findAll("div",class_='zg_itemRow')

length=len(amzn_rank)

for i in range(0,3):

    rank=amzn_rank[i].text


CK = os.getenv("CK")    # Consumer Key
CS = os.getenv("CS")    # Consumer Secret
AT = os.getenv("AT")    # Access Token
AS = os.getenv("AS")    # Accesss Token Secert

print(CK)
print(CS)
print(AT)
print(AS)
# ツイート投稿用のURL
url = "https://api.twitter.com/1.1/statuses/update.json"

# ツイート本文
params = {"status": rank }

# OAuth認証で POST method で投稿
twitter = OAuth1Session(CK, CS, AT, AS)
req = twitter.post(url, params = params)

# レスポンスを確認
if req.status_code == 200:
    print ("OK")
else:
    print ("Error: %d" % req.status_code)
