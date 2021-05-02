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
    t = request.args.get('t',type=int,default=2021)
    qs = None
    if t:
        for i in range(2016,2022):
            if t == i:
                qs = Qs_rank.query.filter_by(time=t).all()
    return render_template('qs_rank.html',qs=qs,t=t)


@app.route('/qs/subject')
def qs_subject():
    t = request.args.get('t',type=int,default=2021)
    s = request.args.get('s',type=str,default='science')
    qs_sub = None
    if s == 'science':
        if t:
            for i in range(2016,2022):
                if t == i:
                    qs_sub = Qs_science_rank.query.filter_by(time=t).all()
    elif s == 'accounting':
        if t:
            for i in range(2016,2022):
                if t == i:
                    qs_sub = Qs_accounting_rank.query.filter_by(time=t).all()

    elif s == 'enginnering':
        if t:
            for i in range(2016,2022):
                if t == i:
                    qs_sub = Qs_engineering_rank.query.filter_by(time=t).all()

    elif s == 'technology':
        if t:
            for i in range(2016,2022):
                if t == i:
                    qs_sub = Qs_technology_rank.query.filter_by(time=t).all()

    return render_template('qs_rank.html',qs_sub=qs_sub,t=t,s=s)



@app.route('/the/')
def the_rank():
    t = request.args.get('t',type=int,default=2021)
    the = None
    if t:
        for i in range(2016,2022):
            if t == i:
                the = The_rank.query.filter_by(time=t).all()
    return render_template('the_rank.html',the=the,t=t)


@app.route('/the/subject')
def the_subject():
    t = request.args.get('t',type=int,default=2021)
    s = request.args.get('s',type=str,default='science')
    the_sub = None
    if s == 'science':
        if t:
            for i in range(2016,2022):
                if t == i:
                    the_sub = The_science_rank.query.filter_by(time=t).all()
    elif s == 'accounting':
        if t:
            for i in range(2016,2022):
                if t == i:
                    the_sub = The_accounting_rank.query.filter_by(time=t).all()

    elif s == 'enginnering':
        if t:
            for i in range(2016,2022):
                if t == i:
                    the_sub = The_engineering_rank.query.filter_by(time=t).all()

    elif s == 'technology':
        if t:
            for i in range(2016,2022):
                if t == i:
                    the_sub = The_technology_rank.query.filter_by(time=t).all()

    return render_template('the_rank.html',the_sub=the_sub,t=t,s=s)



@app.route('/us_news/')
def us_news_rank():
    t = request.args.get('t',type=int,default=2021)
    us = None
    if t:
        for i in range(2016,2022):
            if t == i:
                us = Us_rank.query.filter_by(time=t).all()
    return render_template('us_news_rank.html',us=us,t=t)


@app.route('/us_news/subject')
def us_subject():
    t = request.args.get('t',type=int,default=2021)
    s = request.args.get('s',type=str,default='science')
    us_sub = None
    if s == 'science':
        if t:
            for i in range(2016,2022):
                if t == i:
                    us_sub = Us_science_rank.query.filter_by(time=t).all()
    elif s == 'accounting':
        if t:
            for i in range(2016,2022):
                if t == i:
                    us_sub = Us_accounting_rank.query.filter_by(time=t).all()

    elif s == 'enginnering':
        if t:
            for i in range(2016,2022):
                if t == i:
                    us_sub = Us_engineering_rank.query.filter_by(time=t).all()

    elif s == 'technology':
        if t:
            for i in range(2016,2022):
                if t == i:
                    us_sub = Us_technology_rank.query.filter_by(time=t).all()

    return render_template('us_news_rank.html',us_sub=us_sub,t=t,s=s)




@app.route('/arwu/')
def arwu_rank():
    t = request.args.get('t',type=int,default=2021)
    arwu = None
    if t:
        for i in range(2016,2022):
            if t == i:
                arwu = Arwu_rank.query.filter_by(time=t).all()
    return render_template('arwu_rank.html',arwu=arwu,t=t)


@app.route('/arwu/subject')
def arwu_subject():
    t = request.args.get('t',type=int,default=2021)
    s = request.args.get('s',type=str,default='science')
    arwu_sub = None
    if s == 'science':
        if t:
            for i in range(2016,2022):
                if t == i:
                    arwu_sub = Arwu_science_rank.query.filter_by(time=t).all()
    elif s == 'accounting':
        if t:
            for i in range(2016,2022):
                if t == i:
                    arwu_sub = Arwu_accounting_rank.query.filter_by(time=t).all()

    elif s == 'enginnering':
        if t:
            for i in range(2016,2022):
                if t == i:
                    arwu_sub = Arwu_engineering_rank.query.filter_by(time=t).all()

    elif s == 'technology':
        if t:
            for i in range(2016,2022):
                if t == i:
                    arwu_sub = Arwu_technology_rank.query.filter_by(time=t).all()

    return render_template('arwu_rank.html',arwu_sub=arwu_sub,t=t,s=s)



if __name__ == '__main__':
    app.run()
