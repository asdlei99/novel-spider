# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 11:04:57 2017
@author: zhang
"""


#小说第一面的网址
url="https://www.qu.la/book/26974/9765888.html"
#all1表示想要爬取多少面
all1=860
#path是你想要保存的文件名，可以是绝对路径
path = "超维术士.txt"




next=url.split('/')[-1]
url0 = url.replace(next,"")
from bs4 import BeautifulSoup
import requests
import time
time0=time.time()
header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36"}
a=""
i=0
def replace(content):
    content=content.replace("<br/>\u3000\u3000<br/>\u3000\u3000\xa0\xa0\xa0\xa0","\r\n")
    content=content.replace("[<div id=\"content\">\r\n\t\t\t\t\xa0\xa0\xa0\xa0","\r\n")
    content=content.replace("\t\t\t\t<script>chaptererror();</script>\n</div>]","")
    content=content.replace("<br/>\u3000\u3000","\r\n")
    content=content.replace("[<div id=\"content\">","\r\n")
    content=content.replace("\t\t\t\t<script>chaptererror();</script>\n</br></div>]","")
    return content
while 1:
    url=url0+next
    try :
        r=requests.get(url,timeout=10,headers=header)
    except:
        continue
    r.raise_for_status()
    if  not r.status_code ==200:
              print("产生异常1")
    r.encoding=r.apparent_encoding
    demo=r.text
    soup = BeautifulSoup(demo,"html.parser")
    title =str(soup.h1.string)
    a+=title
    content =str(soup.select("#content"))
    content=replace(content)
    a+=content
    try:
     next= soup.find('a','next').attrs['href']
    except:
        break
    i+=1
    time1=time.time()
    print("\r当前进度:  {0:.2f}% 总花费时间:{1:.2f}s".format(i*100/all1,time1-time0),end="")
    if i>=all1:
        break
print("\n共爬取了{0}章内容,花时{1:.2f}s".format(all1,time1-time0))
g=open(path,mode='w',encoding='utf-8')
g.write(a)
g.close()