#server.py
#-*- coding:utf-8 -*-
from wsgiref.simple_server import make_server
from wsgihello import application
httpd = make_server('localhost',8000,application)
print "Serving HTTP on port 8000"
httpd.serve_forever()
