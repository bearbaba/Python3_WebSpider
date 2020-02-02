import requests
import re
import bs4
import sys
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"}

top = open("top.txt", "w", encoding="utf-8")

no=1
page=1
while no<=150:
    url = "http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-"+str(page)
    response=requests.get(url)
    bsobj=bs4.BeautifulSoup(response.text.encode(encoding="utf-8").decode(encoding="utf-8"))
    elem=bsobj.select(".name")
    pattern=re.compile("[\u4e00-\u9fa5]{1,}")
    for i in elem:
        han_word=re.search(pattern,i.getText()).group(0)
        top.write("top"+str(no)+":  "+str(han_word)+"\n")
        print("已下载：{:.2%}".format(no/150),end="\r")
        if no==150:
            sys.exit(0)    
        no+=1
    page+=1
top.close()
