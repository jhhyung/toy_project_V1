import urllib3
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.legoland.kr/%EC%A6%90%EA%B8%B8%EA%B1%B0%EB%A6%AC/%ED%85%8C%EB%A7%88-%ED%8C%8C%ED%81%AC/%EB%9D%BC%EC%9D%B4%EB%93%9C-%EC%96%B4%ED%8A%B8%EB%9E%99%EC%85%98/bricktopia/',headers=headers)

from pymongo import MongoClient
import certifi

client = MongoClient('mongodb+srv://doha:doha@cluster0.ycsvn.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=certifi.where())
db = client.dbsparta


soup = BeautifulSoup(data.text, 'html.parser')


imgs = soup.find_all(class_='event-show-overview-page__item__image media-block__image')



for img in imgs :
    attr = img.img['data-src']
    url = 'https://www.legoland.kr/'
    url_img = url + attr
    doc = {
        'url': url_img
    }
    db.legoland.insert_one(doc)

title = soup.find_all(class_="header--small")

for title1 in title:
    doc = {
        'title':title1.text
    }
    db.legoland.insert_one(doc)

contents = soup.find_all(class_="media-block__content__text stack")

for a in contents:
    contents1 = a.p.text
    doc = {
        'contents': contents1
    }
    db.legoland.insert_one(doc)





