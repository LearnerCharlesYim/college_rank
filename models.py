# -*- coding:utf-8 -*-
# @Time   :2021/5/1 23:02
# @Author :CharlesYim
# @File   :models.py
from exts import db


class Qs_rank(db.Model):
    __tablename__ = 'qs_rank'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    sea = db.Column(db.Integer)
    chinese_name = db.Column(db.String(100))
    name = db.Column(db.String(100))
    chinese_country = db.Column(db.String(100))
    country = db.Column(db.String(100))
    link = db.Column(db.String(9999))
    total_points = db.Column(db.Float)
    time = db.Column(db.Integer)

class Qs_accounting_rank(db.Model):
    __tablename__ = 'qs_accounting_rank'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    sea = db.Column(db.Integer)
    chinese_name = db.Column(db.String(100))
    name = db.Column(db.String(100))
    chinese_country = db.Column(db.String(100))
    country = db.Column(db.String(100))
    link = db.Column(db.String(9999))
    total_points = db.Column(db.Float)
    time = db.Column(db.Integer)

class Qs_engineering_rank(db.Model):
    __tablename__ = 'qs_engineering_rank'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    sea = db.Column(db.Integer)
    chinese_name = db.Column(db.String(100))
    name = db.Column(db.String(100))
    chinese_country = db.Column(db.String(100))
    country = db.Column(db.String(100))
    link = db.Column(db.String(9999))
    total_points = db.Column(db.Float)
    time = db.Column(db.Integer)


class Qs_science_rank(db.Model):
    __tablename__ = 'qs_science_rank'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    sea = db.Column(db.Integer)
    chinese_name = db.Column(db.String(100))
    name = db.Column(db.String(100))
    chinese_country = db.Column(db.String(100))
    country = db.Column(db.String(100))
    link = db.Column(db.String(9999))
    total_points = db.Column(db.Float)
    time = db.Column(db.Integer)


class Qs_technology_rank(db.Model):
    __tablename__ = 'qs_technology_rank'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    sea = db.Column(db.Integer)
    chinese_name = db.Column(db.String(100))
    name = db.Column(db.String(100))
    chinese_country = db.Column(db.String(100))
    country = db.Column(db.String(100))
    link = db.Column(db.String(9999))
    total_points = db.Column(db.Float)
    time = db.Column(db.Integer)


class The_rank(db.Model):
    __tablename__ = 'the_rank'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sea = db.Column(db.Integer)
    chinese_name = db.Column(db.String(100))
    name = db.Column(db.String(100))
    chinese_country = db.Column(db.String(100))
    country = db.Column(db.String(100))
    link = db.Column(db.String(9999))
    total_points = db.Column(db.Float)
    time = db.Column(db.Integer)


class The_accounting_rank(db.Model):
    __tablename__ = 'the_accounting_rank'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sea = db.Column(db.Integer)
    chinese_name = db.Column(db.String(100))
    name = db.Column(db.String(100))
    chinese_country = db.Column(db.String(100))
    country = db.Column(db.String(100))
    link = db.Column(db.String(9999))
    total_points = db.Column(db.Float)
    time = db.Column(db.Integer)


class The_engineering_rank(db.Model):
    __tablename__ = 'the_engineering_rank'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sea = db.Column(db.Integer)
    chinese_name = db.Column(db.String(100))
    name = db.Column(db.String(100))
    chinese_country = db.Column(db.String(100))
    country = db.Column(db.String(100))
    link = db.Column(db.String(9999))
    total_points = db.Column(db.Float)
    time = db.Column(db.Integer)


class The_science_rank(db.Model):
    __tablename__ = 'the_science_rank'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sea = db.Column(db.Integer)
    chinese_name = db.Column(db.String(100))
    name = db.Column(db.String(100))
    chinese_country = db.Column(db.String(100))
    country = db.Column(db.String(100))
    link = db.Column(db.String(9999))
    total_points = db.Column(db.Float)
    time = db.Column(db.Integer)


class The_technology_rank(db.Model):
    __tablename__ = 'the_technology_rank'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sea = db.Column(db.Integer)
    chinese_name = db.Column(db.String(100))
    name = db.Column(db.String(100))
    chinese_country = db.Column(db.String(100))
    country = db.Column(db.String(100))
    link = db.Column(db.String(9999))
    total_points = db.Column(db.Float)
    time = db.Column(db.Integer)





class Us_rank(db.Model):
    __tablename__ = 'us_rank'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sea = db.Column(db.Integer)
    chinese_name = db.Column(db.String(100))
    name = db.Column(db.String(100))
    chinese_country = db.Column(db.String(100))
    country = db.Column(db.String(100))
    link = db.Column(db.String(9999))
    total_points = db.Column(db.Float)
    time = db.Column(db.Integer)


class Us_accounting_rank(db.Model):
    __tablename__ = 'us_accounting_rank'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sea = db.Column(db.Integer)
    chinese_name = db.Column(db.String(100))
    name = db.Column(db.String(100))
    chinese_country = db.Column(db.String(100))
    country = db.Column(db.String(100))
    link = db.Column(db.String(9999))
    total_points = db.Column(db.Float)
    time = db.Column(db.Integer)


class Us_engineering_rank(db.Model):
    __tablename__ = 'us_engineering_rank'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sea = db.Column(db.Integer)
    chinese_name = db.Column(db.String(100))
    name = db.Column(db.String(100))
    chinese_country = db.Column(db.String(100))
    country = db.Column(db.String(100))
    link = db.Column(db.String(9999))
    total_points = db.Column(db.Float)
    time = db.Column(db.Integer)


class Us_science_rank(db.Model):
    __tablename__ = 'us_science_rank'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sea = db.Column(db.Integer)
    chinese_name = db.Column(db.String(100))
    name = db.Column(db.String(100))
    chinese_country = db.Column(db.String(100))
    country = db.Column(db.String(100))
    link = db.Column(db.String(9999))
    total_points = db.Column(db.Float)
    time = db.Column(db.Integer)


class Us_technology_rank(db.Model):
    __tablename__ = 'us_technology_rank'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sea = db.Column(db.Integer)
    chinese_name = db.Column(db.String(100))
    name = db.Column(db.String(100))
    chinese_country = db.Column(db.String(100))
    country = db.Column(db.String(100))
    link = db.Column(db.String(9999))
    total_points = db.Column(db.Float)
    time = db.Column(db.Integer)



class Arwu_rank(db.Model):
    __tablename__ = 'arwu_rank'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sea = db.Column(db.Integer)
    chinese_name = db.Column(db.String(100))
    name = db.Column(db.String(100))
    chinese_country = db.Column(db.String(100))
    country = db.Column(db.String(100))
    link = db.Column(db.String(9999))
    total_points = db.Column(db.Float)
    time = db.Column(db.Integer)


class Arwu_accounting_rank(db.Model):
    __tablename__ = 'arwu_accounting_rank'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sea = db.Column(db.Integer)
    chinese_name = db.Column(db.String(100))
    name = db.Column(db.String(100))
    chinese_country = db.Column(db.String(100))
    country = db.Column(db.String(100))
    link = db.Column(db.String(9999))
    total_points = db.Column(db.Float)
    time = db.Column(db.Integer)


class Arwu_engineering_rank(db.Model):
    __tablename__ = 'arwu_engineering_rank'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sea = db.Column(db.Integer)
    chinese_name = db.Column(db.String(100))
    name = db.Column(db.String(100))
    chinese_country = db.Column(db.String(100))
    country = db.Column(db.String(100))
    link = db.Column(db.String(9999))
    total_points = db.Column(db.Float)
    time = db.Column(db.Integer)


class Arwu_science_rank(db.Model):
    __tablename__ = 'arwu_science_rank'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sea = db.Column(db.Integer)
    chinese_name = db.Column(db.String(100))
    name = db.Column(db.String(100))
    chinese_country = db.Column(db.String(100))
    country = db.Column(db.String(100))
    link = db.Column(db.String(9999))
    total_points = db.Column(db.Float)
    time = db.Column(db.Integer)


class Arwu_technology_rank(db.Model):
    __tablename__ = 'arwu_technology_rank'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sea = db.Column(db.Integer)
    chinese_name = db.Column(db.String(100))
    name = db.Column(db.String(100))
    chinese_country = db.Column(db.String(100))
    country = db.Column(db.String(100))
    link = db.Column(db.String(9999))
    total_points = db.Column(db.Float)
    time = db.Column(db.Integer)