# -*- coding: utf-8 -*-
"""
    # @Time    : 2023/2/19 23:07
    # @Author  : 有勇气的牛排
    # @FileName: test.py
"""

from pyhive import hive

con_hive = hive.Connection(host='192.168.56.20', port=10000)

hive_cursor = con_hive.cursor()

hive_cursor.execute("select * from cs.article_nopar")
res = hive_cursor.fetchall()
print(res)
