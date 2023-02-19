# -*- coding: utf-8 -*-
"""
    # @Time    : 2023/2/19 23:07
    # @Author  : 有勇气的牛排
    # @FileName: test.py
"""

import paramiko

host = "192.168.56.20"
port = 22
username = "root"
password = "root"

# 登录
trans = paramiko.Transport(host, port)
trans.connect(username=username, password=password)

# 连接客户端
client = paramiko.SFTPClient.from_transport(trans)

source_path = "/usr/local"
# 获取文件列表
res = client.listdir(source_path)
print(res)

client.close() if client is not None else ""

if __name__ == "__main__":
    print(666)
