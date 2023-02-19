# -*- coding: utf-8 -*-
"""
    # @Time    : 2023/2/19 23:07
    # @Author  : 有勇气的牛排
    # @FileName: test.py
"""
import pymysql

db = pymysql.connect(host='127.0.0.1',
                     port=3306,
                     user='root',
                     password='root123456',
                     database='cs_blog')
con = db.cursor()
con.execute("select 1")
res = con.fetchall()
print(res)

# import mysql.connector
#
# db = mysql.connector.connect(
#     port=3306,
#     user='root',
#     password='root123456',
# )
# print(db)
