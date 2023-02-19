# -*- coding: utf-8 -*-
"""
    # @Time    : 2023/2/19 23:07
    # @Author  : 有勇气的牛排
    # @FileName: test.py
"""

from furl import furl

# 1. 解析参数
f = furl('http://www.lgch.com/nocode.php?id=ddb5f1d0338d4b26b86cca8afe270355&vcode=0')
t = f.args
print(t)
print(t['id'])
# 输出 {'id': 'ddb5f1d0338d4b26b86cca8afe270355', 'vcode': '0'}
# 输出 ddb5f1d0338d4b26b86cca8afe270355

# 2. 增加参数
m = furl('www.baidu.com/?a=123').add({'b': '123'}).url
print(m)
# 输出 www.baidu.com/?a=123&b=123

# 3. 删除参数
f = furl('http://www.lgch.com/nocode.php?id=ddb5f1d0338d4b26b86cca8afe270355&vcode=0')
del f.args['vcode']
print(f.args)
# 输出 {'id': 'ddb5f1d0338d4b26b86cca8afe270355'}

# 4. 修改参数
f = furl('http://www.lgch.com/nocode.php?id=ddb5f1d0338d4b26b86cca8afe270355&vcode=0')
f.args['vcode'] = '666'
print(f.args)
# 输出 {'id': 'ddb5f1d0338d4b26b86cca8afe270355', 'vcode': '666'}

# 5. 删除指定参数
n = furl('www.baidu.com/?a=123&b=123').remove('b').url
print(n)
# 输出 www.baidu.com/?b=123

# 6. 获取路径
p = furl('www.baidu.com/a/b/c/?a=123&b=123')
print(p.path)
# 输出 www.baidu.com/a/b/c/

# 7. 设置路径
p = furl('www.baidu.com/a/b/c/?a=123&b=123')
p.path = 'm/m/m/m'
print(p.url)
# 输出 m/m/m/m?a=123&b=123

# 8. 分割参数 ->列表
f = furl('http://www.lgch.com/nocode.php?id=ddb5f1d0338d4b26b86cca8afe270355&vcode=0')
paths = str(f.path)
a = paths.split('/')
print(a)
print(a[1])
# 输出 ['', 'nocode.php']
# 输出 nocode.php
