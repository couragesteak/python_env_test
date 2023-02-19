# -*- coding: utf-8 -*-
"""
    # @Time    : 2023/2/19 23:07
    # @Author  : 有勇气的牛排
    # @FileName: test.py
"""

from pyhive import hive


class UtilHive:
    def __init__(self, host, port, username=None, password=None):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.cursor = self.get_cursor()

    def get_cursor(self):
        con = hive.Connection(host=self.host, port=self.port,
                              username=self.username, password=self.password)
        return con.cursor()

    def execute(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()


utilHive = UtilHive(host='192.168.56.20', port=10000)
res = utilHive.execute("select * from cs.article_nopar")
utilHive.close()
print(res)
