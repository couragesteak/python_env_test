# -*- coding: utf-8 -*-
"""
    # @Time    : 2023/2/19 23:07
    # @Author  : 有勇气的牛排
    # @FileName: test.py
"""

from flask import Flask, render_template
from flask_cors import *
import jinja2

app = Flask(__name__)

CORS(app, supports_credentials=True)


@app.route('/')
@cross_origin()
def index():
    return 'hello world！'


if __name__ == '__main__':
    app.run()
