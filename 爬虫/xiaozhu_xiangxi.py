import requests
from bs4 import BeautifulSoup
import re




def write_oneline(url):
    html = requests.get(url)
    html = html.text


    soup=BeautifulSoup(html,"html.parser")

    titles=soup.select("body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > h4 > em")
    for title in titles:
        title1=title.get_text()
    print(title1)

    addresses=soup.select("body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span")
    for address in addresses:
        address1=(address.get_text())

    leixings=soup.select("#introduce > li.border_none > h6")
    for leixing in leixings:
        leixing1=leixing.get_text()

    house_sizes=soup.select("#introduce > li.border_none > p")
    for house_size in house_sizes:
        house_size1=house_size.get_text()

    print("成功写入1条")
    with open("xiaozhupachong.txt","a",encoding="UTF-8") as fh:
        fh.write("标题: "+title1+"\t")
        fh.write("地址: "+address1+"\t")
        fh.write("房屋类型: "+leixing1+"\t")
        fh.write("房屋大小: "+house_size1+"\t")
        fh.write("房屋链接: "+url+"\t")







def get_url():
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
}
    html = requests.get("https://bj.xiaozhu.com/",headers=headers)
    html=html.text
    zhenze='<a target="_blank" href="(.*?)" class="resule_img_a">'
    addresses=re.compile(zhenze).findall(html)
    print(addresses)
    for address in addresses:
        write_oneline(address)


get_url()


