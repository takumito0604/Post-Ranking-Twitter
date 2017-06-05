#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from requests_oauthlib import OAuth1Session
from bs4 import BeautifulSoup as BS
import requests
import urllib



url='https://www.amazon.co.jp/gp/bestsellers/instant-video'

amzn=requests.get(url)

soup=BS(amzn.text,"lxml")

amzn_rank=soup.findAll("div",class_='zg_itemRow')

length=len(amzn_rank)

for i in range(2):

    rank=amzn_rank[i].text



Ck = os.getenv('CK')    # Consumer Key
Cs = os.getenv('CS')    # Consumer Secret
At = os.getenv('AT')    # Access Token
As = os.getenv('AS')    # Accesss Token Secert


# ツイート投稿用のURL
url = "https://api.twitter.com/1.1/statuses/update.json"

# ツイート本文
params = {"status": rank }

# OAuth認証で POST method で投稿
twitter = OAuth1Session(Ck, Cs, At, As)
req = twitter.post(url, params = params)
print(params)

# レスポンスを確認
if req.status_code == 200:
    print ("OK")
else:
    print ("Error: %d" % req.status_code)
