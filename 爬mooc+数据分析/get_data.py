
el_name_sum = []
el_lang_sum = []
el_level_sum = []
el_heat_sum = []


class Spider():
    def get_content(self, response):
        import bs4
        import re
        bsobj = bs4.BeautifulSoup(response)
        el_name = bsobj.select("h1.courselist-title a")
        for i in el_name:
            el_name_sum.append(i.get_text())
        el_lang = bsobj.select(".courselang")
        for i in el_lang:
            el_lang_sum.append(i.get_text())
        el_level = bsobj.select("div.courselist-meta>span+span")
        for i in el_level:
            pattern = re.compile(".{1,2}（.{2,3}）")
            if re.match(pattern, i.get_text()) != None:
                el_level_sum.append(i.get_text())
            pattern = re.compile(".{2} [0-9]{1,},?[0-9]{1,}")
            if re.match(pattern, i.get_text()) != None:
                el_heat_sum.append(i.get_text())

    def get_responses(self, url):
        import requests

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0 Win64x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'''}
        response = requests.get(url, headers=headers)
        print(response.status_code)
        html=open("mooc"+url[-1]+".html","w",encoding="utf-8")
        html.write(response.text)
        html.close()
        self.get_content(response.text)


    def get_urls(self):
        urls = []
        for i in range(1, 8):
            url = "https://www.mooc.cn/data-science/page/{}".format(i)
            urls.append(url)
        return urls

    def save(self):
        import xlwt
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('sheet1')
        sheet.write(0, 0, '课程名称')
        sheet.write(0, 1, '课程语言')
        sheet.write(0, 2, '课程难度')
        sheet.write(0, 3, '课程热度')
        for i in range(1, len(el_name_sum)+1):
            sheet.write(i, 0, el_name_sum[i-1])
            sheet.write(i, 1, el_lang_sum[i-1])
            sheet.write(i, 2, el_level_sum[i-1])
            sheet.write(i, 3, el_heat_sum[i-1])

        workbook.save(
            r'D:\computer_language\Python_Study\Python_爬虫\爬mooc+数据分析\mooc.xlsx')

    def show(self):
        import pandas as pd
        pd.read_excel('mooc.xlsx')
        print(pd)


if __name__ == "__main__":
    s = Spider()
    for i in s.get_urls():
        s.get_responses(i)
    s.save()
    #s.show()
