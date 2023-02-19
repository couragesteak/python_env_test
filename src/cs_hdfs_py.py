# -*- coding: utf-8 -*-
"""
    # @Time    : 2023/2/19 23:07
    # @Author  : 有勇气的牛排
    # @FileName: test.py
"""

import pyhdfs

client = pyhdfs.HdfsClient(hosts='192.168.56.20:50070', user_name='root')

print(client.get_active_namenode())
res = client.open("/test/info.txt")
print(res.read())
