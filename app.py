from flask import Flask,render_template,request
from models import *
from exts import db
import pyecharts.options as opts
from pyecharts.charts import Line
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
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/qs/')
def qs_rank():
    page = request.args.get(get_page_parameter(), type=int, default=1)
    start = (page - 1) * 10
    end = start + 10
    t = request.args.get('t',type=int,default=2021)
    qs = None
    total = None
    if t:
        for i in range(2016,2022):
            if t == i:
                qs = Qs_rank.query.filter_by(time=t).slice(start, end)
                total = Qs_rank.query.filter_by(time=t).count()
    pagination = Pagination(bs_version=4, page=page, total=total, outer_window=0, inner_window=2)
    return render_template('qs_rank.html',qs=qs,t=t,pagination=pagination)


@app.route('/qs/subject')
def qs_subject():
    page = request.args.get(get_page_parameter(), type=int, default=1)
    start = (page - 1) * 10
    end = start + 10
    t = request.args.get('t',type=int,default=2021)
    s = request.args.get('s',type=str,default='science')
    qs_sub = None
    total = None
    if s == 'science':
        if t:
            for i in range(2016,2022):
                if t == i:
                    qs_sub = Qs_science_rank.query.filter_by(time=t).slice(start, end)
                    total = Qs_science_rank.query.filter_by(time=t).count()
    elif s == 'accounting':
        if t:
            for i in range(2016,2022):
                if t == i:
                    qs_sub = Qs_accounting_rank.query.filter_by(time=t).slice(start, end)
                    total = Qs_science_rank.query.filter_by(time=t).count()

    elif s == 'enginnering':
        if t:
            for i in range(2016,2022):
                if t == i:
                    qs_sub = Qs_engineering_rank.query.filter_by(time=t).slice(start, end)
                    total = Qs_science_rank.query.filter_by(time=t).count()

    elif s == 'technology':
        if t:
            for i in range(2016,2022):
                if t == i:
                    qs_sub = Qs_technology_rank.query.filter_by(time=t).slice(start, end)
                    total = Qs_science_rank.query.filter_by(time=t).count()
    pagination = Pagination(bs_version=4, page=page, total=total, outer_window=0, inner_window=2)
    return render_template('qs_rank.html',qs_sub=qs_sub,t=t,s=s,pagination=pagination)



@app.route('/the/')
def the_rank():
    page = request.args.get(get_page_parameter(), type=int, default=1)
    start = (page - 1) * 10
    end = start + 10
    t = request.args.get('t',type=int,default=2021)
    the = None
    total = None
    if t:
        for i in range(2016,2022):
            if t == i:
                the = The_rank.query.filter_by(time=t).slice(start,end)
                total = The_rank.query.filter_by(time=t).count()
    pagination = Pagination(bs_version=4, page=page, total=total, outer_window=0, inner_window=2)
    return render_template('the_rank.html',the=the,t=t,pagination=pagination)


@app.route('/the/subject')
def the_subject():
    page = request.args.get(get_page_parameter(), type=int, default=1)
    start = (page - 1) * 10
    end = start + 10
    t = request.args.get('t',type=int,default=2021)
    s = request.args.get('s',type=str,default='science')
    the_sub = None
    total = None
    if s == 'science':
        if t:
            for i in range(2016,2022):
                if t == i:
                    the_sub = The_science_rank.query.filter_by(time=t).slice(start,end)
                    total = The_science_rank.query.filter_by(time=t).count()
    elif s == 'accounting':
        if t:
            for i in range(2016,2022):
                if t == i:
                    the_sub = The_accounting_rank.query.filter_by(time=t).slice(start,end)
                    total = The_science_rank.query.filter_by(time=t).count()

    elif s == 'enginnering':
        if t:
            for i in range(2016,2022):
                if t == i:
                    the_sub = The_engineering_rank.query.filter_by(time=t).slice(start,end)
                    total = The_science_rank.query.filter_by(time=t).count()

    elif s == 'technology':
        if t:
            for i in range(2016,2022):
                if t == i:
                    the_sub = The_technology_rank.query.filter_by(time=t).slice(start,end)
                    total = The_science_rank.query.filter_by(time=t).count()
    pagination = Pagination(bs_version=4, page=page, total=total, outer_window=0, inner_window=2)
    return render_template('the_rank.html',the_sub=the_sub,t=t,s=s,pagination=pagination)



@app.route('/us_news/')
def us_news_rank():
    page = request.args.get(get_page_parameter(), type=int, default=1)
    start = (page - 1) * 10
    end = start + 10
    t = request.args.get('t',type=int,default=2021)
    us = None
    total = None
    if t:
        for i in range(2016,2022):
            if t == i:
                us = Us_rank.query.filter_by(time=t).slice(start,end)
                total = Us_rank.query.filter_by(time=t).count()
    pagination = Pagination(bs_version=4, page=page, total=total, outer_window=0, inner_window=2)
    return render_template('us_news_rank.html',us=us,t=t,pagination=pagination)


@app.route('/us_news/subject')
def us_subject():
    page = request.args.get(get_page_parameter(), type=int, default=1)
    start = (page - 1) * 10
    end = start + 10
    t = request.args.get('t',type=int,default=2021)
    s = request.args.get('s',type=str,default='science')
    us_sub = None
    total = None
    if s == 'science':
        if t:
            for i in range(2016,2022):
                if t == i:
                    us_sub = Us_science_rank.query.filter_by(time=t).slice(start,end)
                    total = Us_science_rank.query.filter_by(time=t).count()
    elif s == 'accounting':
        if t:
            for i in range(2016,2022):
                if t == i:
                    us_sub = Us_accounting_rank.query.filter_by(time=t).slice(start,end)
                    total = Us_science_rank.query.filter_by(time=t).count()

    elif s == 'enginnering':
        if t:
            for i in range(2016,2022):
                if t == i:
                    us_sub = Us_engineering_rank.query.filter_by(time=t).slice(start,end)
                    total = Us_science_rank.query.filter_by(time=t).count()

    elif s == 'technology':
        if t:
            for i in range(2016,2022):
                if t == i:
                    us_sub = Us_technology_rank.query.filter_by(time=t).slice(start,end)
                    total = Us_science_rank.query.filter_by(time=t).count()
    pagination = Pagination(bs_version=4, page=page, total=total, outer_window=0, inner_window=2)
    return render_template('us_news_rank.html',us_sub=us_sub,t=t,s=s,pagination=pagination)




@app.route('/arwu/')
def arwu_rank():
    page = request.args.get(get_page_parameter(), type=int, default=1)
    start = (page - 1) * 10
    end = start + 10
    t = request.args.get('t',type=int,default=2021)
    arwu = None
    total = None
    if t:
        for i in range(2016,2022):
            if t == i:
                arwu = Arwu_rank.query.filter_by(time=t).slice(start,end)
                total = Arwu_rank.query.filter_by(time=t).count()
    pagination = Pagination(bs_version=4, page=page, total=total, outer_window=0, inner_window=2)
    return render_template('arwu_rank.html',arwu=arwu,t=t,pagination=pagination)


@app.route('/arwu/subject')
def arwu_subject():
    page = request.args.get(get_page_parameter(), type=int, default=1)
    start = (page - 1) * 10
    end = start + 10
    t = request.args.get('t',type=int,default=2021)
    s = request.args.get('s',type=str,default='science')
    arwu_sub = None
    total = None
    if s == 'science':
        if t:
            for i in range(2016,2022):
                if t == i:
                    arwu_sub = Arwu_science_rank.query.filter_by(time=t).slice(start,end)
                    total = Arwu_science_rank.query.filter_by(time=t).count()
    elif s == 'accounting':
        if t:
            for i in range(2016,2022):
                if t == i:
                    arwu_sub = Arwu_accounting_rank.query.filter_by(time=t).slice(start,end)
                    total = Arwu_science_rank.query.filter_by(time=t).count()

    elif s == 'enginnering':
        if t:
            for i in range(2016,2022):
                if t == i:
                    arwu_sub = Arwu_engineering_rank.query.filter_by(time=t).slice(start,end)
                    total = Arwu_science_rank.query.filter_by(time=t).count()

    elif s == 'technology':
        if t:
            for i in range(2016,2022):
                if t == i:
                    arwu_sub = Arwu_technology_rank.query.filter_by(time=t).slice(start,end)
                    total = Arwu_science_rank.query.filter_by(time=t).count()
    pagination = Pagination(bs_version=4, page=page, total=total, outer_window=0, inner_window=2)
    return render_template('arwu_rank.html',arwu_sub=arwu_sub,t=t,s=s,pagination=pagination)


@app.route('/qs/trend/')
def qs_trend():
    items = db.session.query(Qs_rank.chinese_name).order_by(Qs_rank.sea).all()
    data1 = []
    for item in items:
        data1.append(item[0])
    data2 = set(data1)
    colleges = list(data2)
    result = None
    c = request.args.get('college',type=str,default='')

    return render_template('qs_trend.html',colleges=colleges,name=c)


def line_base(name,result):
    c = (
        Line()

            .add_xaxis([str(item[1]) for item in result ])
            .add_yaxis(f"{name}", [str(item[0]) for item in result])
            .set_global_opts(title_opts=opts.TitleOpts(title="排名趋势"))

    )
    return c


@app.route("/qs/lineChart/")
def get_line_qs_chart():
    college = request.args.get('college')
    result = db.session.query(Qs_rank.sea, Qs_rank.time).filter_by(chinese_name=f'{college}').order_by(Qs_rank.time).all()

    c = line_base(college,result)
    return c.dump_options_with_quotes()


@app.route('/the/trend/')
def the_trend():
    items = db.session.query(The_rank.chinese_name).order_by(The_rank.sea).all()
    data1 = []
    for item in items:
        data1.append(item[0])
    data2 = set(data1)
    colleges = list(data2)

    c = request.args.get('college',type=str,default='')

    return render_template('the_trend.html',colleges=colleges,name=c)


@app.route("/the/lineChart/")
def get_line_the_chart():
    college = request.args.get('college')
    result = db.session.query(The_rank.sea, The_rank.time).filter_by(chinese_name=f'{college}').order_by(The_rank.time).all()

    c = line_base(college,result)
    return c.dump_options_with_quotes()


@app.route('/us_news/trend/')
def us_trend():
    items = db.session.query(Us_rank.chinese_name).order_by(Us_rank.sea).all()
    data1 = []
    for item in items:
        data1.append(item[0])
    data2 = set(data1)
    colleges = list(data2)
    c = request.args.get('college',type=str,default='')

    return render_template('us_news_trend.html',colleges=colleges,name=c)

@app.route("/us_news/lineChart/")
def get_line_us_chart():
    college = request.args.get('college')
    result = db.session.query(Us_rank.sea, Us_rank.time).filter_by(chinese_name=f'{college}').order_by(Us_rank.time).all()

    c = line_base(college,result)
    return c.dump_options_with_quotes()



@app.route('/arwu/trend/')
def arwu_trend():
    items = db.session.query(Arwu_rank.chinese_name).order_by(Arwu_rank.sea).all()
    data1 = []
    for item in items:
        data1.append(item[0])
    data2 = set(data1)
    colleges = list(data2)
    c = request.args.get('college',type=str,default='')

    return render_template('arwu_trend.html',colleges=colleges,name=c)

@app.route("/arwu/lineChart/")
def get_line_arwu_chart():
    college = request.args.get('college')
    result = db.session.query(Arwu_rank.sea, Arwu_rank.time).filter_by(chinese_name=f'{college}').order_by(Arwu_rank.time).all()

    c = line_base(college,result)
    return c.dump_options_with_quotes()


@app.route('/search/')
def search():
    college = request.args.get('kw')

    if Qs_rank.query.filter_by(chinese_name=f'{college}').all() or The_rank.query.filter_by(chinese_name=f'{college}').all() or Us_rank.query.filter_by(chinese_name=f'{college}').all() or Arwu_rank.query.filter_by(chinese_name=f'{college}').all():
        return render_template('search.html',college=college)
    else:
        return render_template('search.html', massage='暂无学校信息')

@app.route('/qs/map/')
def map_qs():
    return render_template('qs_map.html',qs_map='qs_map')

@app.route('/the/map/')
def map_the():
    return render_template('the_map.html',the_map='the_map')

@app.route('/us_news/map/')
def us_news_qs():
    return render_template('us_news_map.html',us_map='us_map')

@app.route('/arwu/map/')
def map_arwu():
    return render_template('arwu_map.html',arwu_map='arwu_map')


from pyecharts import options as opts
from pyecharts.charts import Map

def map_base(colleges_list):

    c = (
        Map()
        .add("university", colleges_list, maptype="world")
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="大学分布图"),
            visualmap_opts=opts.VisualMapOpts(max_=200),
        )

    )
    return c

@app.route('/get_map/<name>')
def get_map(name):
    colleges = None
    if name == 'qs':
        colleges = db.session.query(Qs_rank.country,Qs_rank.name).order_by(Qs_rank.country).all()
    elif name == 'the':
        colleges = db.session.query(The_rank.country,The_rank.name).order_by(The_rank.country).all()
    elif name == 'us_news':
        colleges = db.session.query(Us_rank.country,Us_rank.name).order_by(Us_rank.country).all()
    elif name == 'arwu':
        colleges = db.session.query(Arwu_rank.country,Arwu_rank.name).order_by(Arwu_rank.country).all()


    info = []
    dict_u = {}
    for item in colleges:
        if dict_u == {}:
            dict_u[item[0]] = []
            dict_u[item[0]].append(item[1])
        elif item[0] in dict_u.keys():
            dict_u[item[0]].append(item[1])
        else:
            info.append(dict_u)
            dict_u = {}
            dict_u[item[0]] = []
            dict_u[item[0]].append(item[1])
    info.append(dict_u)

    colleges_list = []
    for dict in info:
        for k,v in dict.items():
            college_list = []
            k = 'China' if k == 'China (Mainland)' else k
            k = 'United States' if k == 'USA' else k
            k = 'United Kingdom' if k == 'UK' else k

            college_list.append(k)
            college_list.append(len(set(v)))
            print(college_list)
            colleges_list.append(college_list)

    c = map_base(colleges_list)
    return c.dump_options_with_quotes()