import requests
from bs4 import BeautifulSoup
import urllib.request
import re
import os
import time

headers={
        "cookie" : 'miid=1296267545453648768; t=b4d385e2145f596a67961e4dd08e9a8f; cna=pqwcFXxbJjACAXWIA7AFEfA8; thw=cn; v=0; cookie2=1b7e32fc526ab419ad9bb0dff7e38db9; _tb_token_=7514beaed3731; unb=4235284520; sg=101; _l_g_=Ug%3D%3D; skt=52f2005f737e3263; cookie1=AnQIvxj44XbyESoVNTVtwfJRB8W%2BbAPV%2BVZMWhAghjk%3D; csg=78ec1478; uc3=vt3=F8dBy3kbhNId9VXzGFY%3D&id2=Vy67WD1MZomrsw%3D%3D&nk2=F5RBzeKtOazPVJc%3D&lg2=W5iHLLyFOGW7aA%3D%3D; existShop=MTU2MTAwNTg0OQ%3D%3D; tracknick=tb487881011; lgc=tb487881011; _cc_=UIHiLt3xSw%3D%3D; dnk=tb487881011; _nk_=tb487881011; cookie17=Vy67WD1MZomrsw%3D%3D; tg=0; enc=%2FTqA3gAexHOKU0cyPYbSWM1pGS8vgnlEK3EMnkYd2T%2BlB%2BJh18hxryREG48c%2BYmdk7yfvbSMCBDQExP23eUm3w%3D%3D; mt=ci=21_1; uc1="cookie15=UtASsssmOIJ0bQ%3D%3D"; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; swfstore=296210; JSESSIONID=0CD9E831B839424E1690ABB52DFA45F8; l=bBMxcfBPv539-Lj2BOCwquIRXZbTjIRYSuPRwk6Hi_5dx6YsTkbOkfDZUFv6Vj5RsnLB4s6vWje9-etks; isg=BIyMWdlaPdTzwihB8roCuKdhXep-bRshzniT3OZNiDfacSx7Dtcv_4LLETlsPGjH',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
global paqucishu
paqucishu=0
def get_one_page(url):
    url.encode("UTF-8")
    urls=requests.get(url,headers=headers)
    urls=urls.text.encode("UTF-8")
    # print(url)
    # print(urls)
    soup=BeautifulSoup(urls,"lxml")
    # print(soup)
    zhengze='"pic_url":"//(.*?)",'
    zhengze_mingzi='"raw_title":"(.*?)",'
    imgs=re.compile(zhengze).findall(str(soup))
    mingzi=re.compile(zhengze_mingzi).findall(str(soup))
    # imgs=soup.select("div > div.pic")
    # print(imgs)
    # print(imgs)
    i=0
    for img,mingzi in zip(imgs,mingzi):
        img="https://"+img
        print(img)
        try:
            time.sleep(0.2)
            file="F:/淘宝图抓取/长裙/"+str(mingzi)+".jpg"
            urllib.request.urlretrieve(img,filename=file)
            print("爬取成功")
            # i=int(i)+1
        except Exception as result:
            print('图片下载失败' + str(result))
def get_one_pages():
    key=input("请输入你想爬取的图片的名称呼种类")
    nums=int(input("请输入你想爬取的页数"))
    for i in range(0,nums):
        key_name=urllib.request.quote(key)
        url="https://s.taobao.com/search?q="+key_name+"&s="+str(int(i)*44)
        # print(url)
        print("开启第")
        print(i)
        print("页爬取")
        time.sleep(1)
        get_one_page(url)

if __name__ == '__main__':
    # print(os.getcwd())
    get_one_pages()






