#regexp.py
#-*- coding:utf-8 -*-
import re
print(re.split(r'\s+','a b   c'))
print(re.split(r'[\s\,]+','a,b, c,  d'))
m = re.match(r'^(\d{3})-(\d{3,8})$','010-12345')
print m.group(0)
print m.group(1)
print m.group(2)
t='19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]5[0-9]|[0-9])$',t)
print m.groups()
print re.match(r'^(\d+)(0*)$','102300').groups()
print re.match(r'^(\d+?)(0*)$','102300').groups()

re_tel = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_tel.match('010-12345').groups())
print(re_tel.match('010-8086').groups())

re_email = re.compile(r'(^([0-9a-zA-Z\_]+)\.([0-9a-zA-Z\_]+)@([0-9a-zA-Z]+)\.([a-zA-Z]{2,5})$)|(^([0-9a-zA-Z\_]+)@([0-9a-zA-Z]+)\.([a-zA-Z]{2,5})$)')
re_email = re.compile(r'(\<[a-zA-Z]+\s+[a-zA-Z]+\>)?\s*(([0-9a-zA-Z\_\-]+\.[0-9a-zA-Z\_\-]+)|([0-9a-zA-Z\_\-]+))@([0-9a-zA-Z\-]+)\.([a-zA-Z\-]{2,5})$')
print re_email.match('<Tom Paris> tom@voyager.org').groups()
print re_email.match('coco.dee@gmail.com').groups()
print re_email.match('cocodee@gmail.com').groups()
print re_email.match('cocodee@163.com').groups()
#unicode regex???