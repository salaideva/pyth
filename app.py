# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 07:29:56 2022

@author: salai
"""
from flask import Flask
from waitress import serve

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello dev!"

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)