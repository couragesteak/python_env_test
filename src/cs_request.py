# -*- coding: utf-8 -*-
"""
    # @Time    : 2023/2/19 23:07
    # @Author  : 有勇气的牛排
    # @FileName: test.py
"""

import requests
from bs4 import BeautifulSoup

url = 'https://www.couragesteak.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Mobile Safari/537.36'
}

res = requests.get(url, headers=headers).content
soup = BeautifulSoup(res, 'lxml')

print(soup.body)
