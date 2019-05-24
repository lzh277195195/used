import requests
import re
from bs4 import BeautifulSoup

def get_one_pag(i):
    html = requests.get('http://www.kugou.com/yy/rank/home/'+str(i)+'-8888.html')
    # print(url)
    list1=[]
    soup=BeautifulSoup(html.text,"lxml")
    times=soup.select("#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_tips_r > span")
    music_name=soup.select("#rankWrap > div.pc_temp_songlist > ul > li > a")
    music_index=soup.select("#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_num")
    # print(times,music_index,music_name)
    for time,music_name1,music_index1 in zip(times,music_name,music_index):
        data={
            "index":list(music_index1.stripped_strings),
            # "index":music_index1,
            "music":music_name1.get_text(),
            # "time":time
            "time":list(time.stripped_strings)
        }
        list1.append(data)
    print(list1)
# #

def get_one_pags():
    for i in range(0,20):
        get_one_pag(i)


get_one_pags()