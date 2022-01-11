# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 10:10:55 2022

@author: salai
"""
from flask import Flask
from waitress import serve

app = Flask(__name__)
import openshift as oc
print('OpenShift client version: {}'.format(oc.get_client_version()))
print('OpenShift server version: {}'.format(oc.get_server_version()))

@app.route('/')
def hello():
    return " <!DOCTYPE html> <html> <head> <title>ANZ </title> </head> <body> <h1>OC login </h1> <p>Automation</p> </body></html> "

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)