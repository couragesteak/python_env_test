# -*- coding: utf-8 -*-
"""
    # @Time    : 2023/2/19 23:07
    # @Author  : 有勇气的牛排
    # @FileName: test.py
"""

import time

from hdfs import Client

client = Client("http://192.168.56.20:50070/")

file_list = client.list("/", status=False)
print(file_list)

# try:
#     res = client.status("/a", strict=False)
#     print(res)
# except Exception as e:
#     print(e)

# res = client.checksum(hdfs_path="/")
# print(res)

# print(client.parts("/"))
# print(client.content("/"))

# client.makedirs(hdfs_path="/test", permission="755")

# client.rename(hdfs_src_path="/test", hdfs_dst_path="/test2")

# print(client.resolve(hdfs_path="article.txt"))

# client.set_replication(hdfs_path="/test/info.txt", replication=2)

# print(client.content("/test/info.txt"))

# res = client.read(hdfs_path="/test/info.txt", encoding='utf-8')
# print(res)
#
# for i in res:
#     print(i)

# client.download(hdfs_path="/test/info.txt", local_path="E:/center/dev")

# with client.read("/test/info.txt", encoding='utf-8') as f:
#     for line in f:
#         print(line)

# client.delete(hdfs_path="/test/info.txt",
#               recursive=False,
#               skip_trash=True)

# client.upload(hdfs_path="/test",
#               local_path="E:/center/dev/info.txt")

# client.set_permission(hdfs_path="/test/info.txt",
#                       permission="755")

client.set_times(hdfs_path="/test/info.txt",
                 access_time=int(time.time()) * 1000,
                 modification_time=int(time.time()) * 1000)

# file_list = client.list("/", status=False)
# print(file_list)
