from readline import read_init_file
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

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
    doc = {
        "star": star_value,
        "opinion": opinion_value
    }
    db.reviews.insert_one(doc)
    return jsonify({'msg':'작성 완료'})


@app.route("/reviews", methods=["GET"])
def upload_comments():
    review_list = list(db.reviews.find({},{'_id':False}))
    return jsonify({'reviews': review_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)