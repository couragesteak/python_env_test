# -*- coding: utf-8 -*-
"""
    # @Time    : 2023/2/19 23:07
    # @Author  : 有勇气的牛排
    # @FileName: test.py
"""

from hdfs import Client

con_hdfs = Client("http://192.168.56.20:50070/")

file_list = con_hdfs.list("/")
print(file_list)
