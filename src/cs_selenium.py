# -*- coding: utf-8 -*-
"""
    # @Time    : 2023/2/19 23:07
    # @Author  : 有勇气的牛排
    # @FileName: test.py
"""

from selenium import webdriver

url = "https://www.baidu.com/"

# 加载驱动
# driver = webdriver.Firefox()   # Firefox浏览器
# driver = webdriver.Firefox("驱动路径")
driver = webdriver.Chrome("E:/center/python_3.6/test/chromedriver.exe")  # Chrome浏览器
# driver = webdriver.Ie()        # Internet Explorer浏览器
# driver = webdriver.Edge()      # Edge浏览器
# driver = webdriver.Opera()     # Opera浏览器
# driver = webdriver.PhantomJS()   # PhantomJS

# 打开网页
driver.get(url)
