from flask import Flask,render_template,request,make_response,send_from_directory,jsonify
from models import *
from exts import db

from flask_paginate import Pagination,get_page_parameter
app = Flask(__name__)

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'college_rank'
USERNAME = 'root'
PASSWORD = 'root'
DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8mb4".format(username=USERNAME,password=PASSWORD,host=HOSTNAME,port=PORT,db=DATABASE)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
# with app.app_context():
#     db.create_all()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/qs/')
def qs_rank():
    qs = Qs_rank.query.filter_by(time=2021).all()
    return render_template('qs_rank.html',qs=qs)

@app.route('/the/')
def the_rank():
    return render_template('the_rank.html')

@app.route('/us_news/')
def us_news_rank():
    return render_template('us_news_rank.html')

@app.route('/arwu/')
def arwu_rank():
    return render_template('arwu_rank.html')

if __name__ == '__main__':
    app.run()
