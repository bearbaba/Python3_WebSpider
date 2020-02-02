import requests
import bs4
import xlwt
import re
workbook = xlwt.Workbook(encoding="utf-8")
worksheet = workbook.add_sheet('sheet1')
worksheet.write(0, 0, '排名')
worksheet.write(0, 1, '电影名称')
worksheet.write(0, 2, '电影评分')
worksheet.write(0, 3, '电影简介')

start=0
end=25
while end<=100:
    header={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36"}
    url = "https://movie.douban.com/top250?start={}&filter=".format(start)
    response=requests.get(url,headers=header)

    bsobj=bs4.BeautifulSoup(response.text)
    name_elem=bsobj.select('div[class="pic"] a img')
    score_elem = bsobj.select('span[class="rating_num"]')
    introduction_elem=bsobj.select('span[class="inq"]')
    for i in range(25):
        worksheet.write(start+i+1,2,score_elem[i].getText())
        worksheet.write(start+i+1,1,name_elem[i].get('alt'))
        worksheet.write(start+i+1,0,start+i+1)
        worksheet.write(start+i+1,3,introduction_elem[i].getText())
        print("已读取{:.2%}".format((start+i+1)/100),end="\r")
    start+=25
    end+=25
print("\n完成")
workbook.save('douban.xlsx')
