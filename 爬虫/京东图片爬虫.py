import requests
from bs4 import BeautifulSoup
import urllib.request
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
url=requests.get("https://channel.jd.com/women.html?cu=true&utm_source=baidu-search&utm_medium=cpc&utm_campaign=t_262767352_baidusearch&utm_term=120052825805_0_46867cf16f5647f1835a8db4bfadedc8",headers=headers)
url=url.text
# print(url)

soup=BeautifulSoup(url,"lxml")
imgs=soup.select('body > div.w.women-floor160419-06 > div > div > ul > li > a > img')
i=0
# print(imgs)
for img in imgs:
    print(img)
    img="http:"+img.get("data-lazy-img")
    print(img)
    try:
        file="F:/淘宝图片抓取/"+str(i)+".jpg"
        urllib.request.urlretrieve(img,filename=file)
        print("爬取成功")
        i=int(i)+1
    except Exception as result:
        print('图片下载失败' + str(result))

