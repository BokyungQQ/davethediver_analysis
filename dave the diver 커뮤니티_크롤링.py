#!/usr/bin/env python
# coding: utf-8

# In[5]:


import csv
import requests
from bs4 import BeautifulSoup


# In[6]:


# 크롤링 데이터를 csv 파일로 저장
with open('데이브더다이버갤러리크롤링.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    # Write header row
    csvwriter.writerow(['글번호', '제목', '댓글 개수', '작성일자', '조회수', '추천'])

    for i in range(288, 295):
        url = f"https://gall.dcinside.com/mgallery/board/lists/?id=davethediver&page={i}"
        params = {'id': 'davethediver'}
        headers = {'User-Agent': ""}
        webpage = requests.get(url, params=params, headers=headers)

        soup = BeautifulSoup(webpage.content, "lxml")
        article = soup.select(".us-post")

        for item in article:
            num = item.select(".gall_num")[0].text
            title = item.select(".ub-word > a")[0].text
            reply = item.select(".ub-word > a.reply_numbox > .reply_num")
            reply_count = reply[0].text if reply else ""
            timestamp = item.select(".gall_date")[0].text
            refresh = item.select(".gall_count")[0].text
            recommend = item.select(".gall_recommend")[0].text

            csvwriter.writerow([num, title, reply_count, timestamp, refresh, recommend])

