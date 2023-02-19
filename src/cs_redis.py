# -*- coding: utf-8 -*-
"""
    # @Time    : 2023/2/19 23:07
    # @Author  : 有勇气的牛排
    # @FileName: test.py
"""
import redis


def redis_connect():
    # redis-py使用connection pool来管理对一个redis server的所有连接，避免每次建立、释放连接的开销。默认，每个Redis实例都会维护一个自己的连接池。
    pool = redis.ConnectionPool(host='127.0.0.1', port=6379, decode_responses=True, db=0)
    red = redis.Redis(connection_pool=pool)
    return red

# 连接到Redis服务器
red = redis_connect()
# red.hset('bigkey', 'smallkey', 'value')

res = red.hget('bigkey', 'smallkey')
print(res)
