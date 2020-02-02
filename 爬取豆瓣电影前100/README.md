<h1 align=center>爬取豆瓣电影排行前一百的电影</h1>

----

本次爬取将内容保存在表格中



##  一、相关库的使用

需要用到requests库、xlwt、bs4库

相关命令：

> <code>  import requests,xlwt,bs4</code>

## 二、分析web

豆瓣排行榜的url为https://movie.douban.com/top250?start=0&filter=，通过分析可知每个页面有25个电影信息，点击下一页时，start=0变为start=25，故可知每个页面通过start而变化



##  三、bs4库的使用

bs4主要用于查找所需HTML标签的内容，例如对页面分析时发现一部电影的名字中含有中文名和其它名（电影原名，比如外国电影就会是外国原名）

![image-20200203005313671](C:\Users\bearbaba\AppData\Roaming\Typora\typora-user-images\image-20200203005313671.png)



在上图中看到电影原名与电影的中文名的标签相同，标签的class属性值相同，故用常规select（）方法查找可能会得到电影的两个名字，然而我们发现电影海报图片的alert属性值是电影的名称，所以我们用

> <code>name_elem=bsobj.select("div[class='pic'] a img")</code><br/><code>name_elem[i].get('alt')</code>

得到alt属性值



##  四、xlwt库的使用

xlwt用于表格的创建，一个表格为工作簿（workbook），表格中含有sheet，sheet中有大量单元格（cell）

首先是工作簿创建，<code>workbook=Workbook()</code>

然后为表格增加sheet，<code>worksheet=workbook.add_sheet("sheet_name")</code>

worksheet(0,0,"cell_content"),worksheet中0,0表示单元格位置（行在前，列在后），cell_content为每个单元格的内容。