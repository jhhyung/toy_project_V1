from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
import certifi
client = MongoClient('mongodb+srv://doha:doha@cluster0.ycsvn.mongodb.net/Cluster0?retryWrites=true&w=majority', tlsCAFile=certifi.where())
db = client.dbsparta

@app.route('/')
def home():
    return render_template('./index.html')

@app.route("/reviews", methods=["POST"])
def comments_post():
    opinion_value = request.form['opinion_value']
    star_value = request.form['star_value']
    num_value = request.form['num_value']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(
        'https://www.legoland.kr/%EC%A6%90%EA%B8%B8%EA%B1%B0%EB%A6%AC/%ED%85%8C%EB%A7%88-%ED%8C%8C%ED%81%AC/%EB%9D%BC%EC%9D%B4%EB%93%9C-%EC%96%B4%ED%8A%B8%EB%9E%99%EC%85%98/',
        headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')
    # content > section > div > div:nth-child(1)
    # 이미지  #content > section > div > div:nth-child(1) > div.event-show-overview-page__item__image.event-show-overview-page__item__image.media-block__image > picture > img
    # 제목   #content > section > div > div:nth-child(1) > div.event-show-overview-page__item__list.media-block__content > div > h2
    attrs = soup.select('#content > section > div > div')

    for attr in attrs:
        tag = attr.select_one('div.event-show-overview-page__item__list.media-block__content > div > h2')
        title = tag.text
        img = attr.select_one(
            'div.event-show-overview-page__item__image.event-show-overview-page__item__image.media-block__image > picture > img')[
            'src']
        full_img = 'https://www.legoland.kr' + img

    doc = {
        "star": star_value,
        "opinion": opinion_value,
        "num": num_value,
        "title": title,
        "img": full_img
    }
    db.reviews.insert_one(doc)
    return jsonify({'msg':'작성 완료'})


@app.route("/reviews", methods=["GET"])
def upload_comments():
    review_list = list(db.reviews.find({},{'_id':False}))
    return jsonify({'reviews': review_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)


