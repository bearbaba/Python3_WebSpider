class Spider():
    def __init__(self):
        self.el_name=[]
        self.el_lang=[]
        self.el_level=[]
        self.el_heat=[]
    def get_content(self): 
        import requests
        import bs4
        import re
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0 Win64x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'''}
        response = requests.get("https://www.mooc.cn/data-science", headers=headers)
        print(response.status_code)
        html=open("mooc.html","w",encoding="utf-8")
        html.write(response.text)
        html.close()
        bsobj=bs4.BeautifulSoup(response.text)
        el_name = bsobj.select("h1.courselist-title a")

        for i in el_name:
            self.el_name.append(i.get_text())
        el_lang = bsobj.select(".courselang")
        for i in el_lang:
            self.el_lang.append(i.get_text())
        el_level = bsobj.select("div.courselist-meta>span+span")
        for i in el_level:
            pattern=re.compile(".{1,2}（.{2}）")
            if re.match(pattern,i.get_text())!=None:
                self.el_level.append(i.get_text())
            pattern=re.compile(".{2} [0-9]{1,},?[0-9]{1,}")
            if re.match(pattern,i.get_text())!=None:
                self.el_heat.append(i.get_text())
    def save(self):
        import xlwt
        workbook=xlwt.Workbook()
        sheet=workbook.add_sheet('sheet1')
        sheet.write(0,0,'课程名称')
        sheet.write(0,1,'课程语言')
        sheet.write(0,2,'课程难度')
        sheet.write(0,3,'课程热度')
        for i in range(1,len(self.el_name)+1):
            sheet.write(i,0,self.el_name[i-1])
            sheet.write(i,1,self.el_lang[i-1])
            sheet.write(i,2,self.el_level[i-1])
            sheet.write(i,3,self.el_heat[i-1])
        workbook.save(r'D:\computer_language\Python_Study\Python_爬虫\爬mooc\mooc.xlsx')
    def show(self):
        import pandas as pd
        pd.read_excel('mooc.xlsx')
        print(pd)
        

if __name__ == "__main__":
    s=Spider()
    s.get_content()
    s.save()
    s.show()
    
