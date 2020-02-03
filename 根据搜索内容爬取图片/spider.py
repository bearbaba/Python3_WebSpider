from selenium import webdriver
import bs4
import requests
import time
driver=webdriver.Chrome()
driver.get("http://image.baidu.com/")
input=driver.find_element_by_css_selector('#kw')
input.send_keys('石原里美')
search=driver.find_element_by_css_selector(".s_search")
search.click()
photos = driver.find_elements_by_class_name("imgitem")
photo_urls=[]
for i in photos:
    photo_urls.append(i.get_attribute('data-objurl'))
print(photo_urls)
cout=1
for i in photo_urls:
    response=requests.get(i)
    photo=open('tupian{}.jpg'.format(str(cout)),'wb')
    photo.write(response.content)
    photo.close()
    cout+=1
