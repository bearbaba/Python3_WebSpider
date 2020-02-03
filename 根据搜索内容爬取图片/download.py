import requests
import bs4
url = "https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=4168939085,388587811&fm=26&gp=0.jpg"
res=requests.get(url)
photo=open('photo.jpg','wb')
photo.write(res.content)
photo.close()
