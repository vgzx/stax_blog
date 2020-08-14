# -*- encoding: utf-8 -*-
'''
@File    : db_util.py
@Author  : vgzx
@Date    : 2020/08/14 22:23
@Contact : viewgrand@163.com
@Desc    : 数据库相关工具

'''

##
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:225216192@127.0.0.1:3306/demo'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    __tablename__ = 'user'
    def __init__(self, name, email):
        self.name = name

    def __repr__(self):
        return '<User %r>' % self.name

ulist = User.query.all()
print(ulist)
