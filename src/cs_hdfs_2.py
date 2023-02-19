# -*- coding: utf-8 -*-
"""
    # @Time    : 2023/2/19 23:07
    # @Author  : 有勇气的牛排
    # @FileName: test.py
"""

from hdfs import Client

# hdfsConn = Client('http://192.168.56.20:50070/', root='', timeout=1000, session=False)
hdfsConn = Client('http://192.168.56.20:50070/', root="/")
# hdfsConn = Client('http://192.168.56.20:9000/')


hdfs_file_path = "/user.txt"

with hdfsConn.read(hdfs_file_path, encoding='utf-8', delimiter='\n') as f:
    for line in f:
        print(line)
        # NearLinearIds.append(line.strip())
