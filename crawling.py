import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.legoland.kr/%EC%A6%90%EA%B8%B8%EA%B1%B0%EB%A6%AC/%ED%85%8C%EB%A7%88-%ED%8C%8C%ED%81%AC/%EB%9D%BC%EC%9D%B4%EB%93%9C-%EC%96%B4%ED%8A%B8%EB%9E%99%EC%85%98/',headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')

#content > section > div > div:nth-child(1)
#이미지  #content > section > div > div:nth-child(1) > div.event-show-overview-page__item__image.event-show-overview-page__item__image.media-block__image > picture > img
#제목   #content > section > div > div:nth-child(1) > div.event-show-overview-page__item__list.media-block__content > div > h2
attrs = soup.select('#content > section > div > div')

for attr in attrs:
    tag = attr.select_one('div.event-show-overview-page__item__list.media-block__content > div > h2')
    title = tag.text
    img = attr.select_one('div.event-show-overview-page__item__image.event-show-overview-page__item__image.media-block__image > picture > img')['src']
    full_img = 'https://www.legoland.kr' + img
    print(full_img, title)