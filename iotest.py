#advance.py 
#-*- coding:utf-8 -*-
#f = open('D:\\fusion docs\\CN Person Employment TDD.doc','rb',80000)
#print f.read(1000)
#f.close()
f = open('.\\gitcommand.txt','r')
#print f.read()
f.close()

try:
    f = open('.\\gitcommand.txt','r')
    #print f.read()
finally:
    if f:
        f.close()

with open('.\\gitcommand.txt','r') as f:
    for line in f.readlines()[:10]:
        #print(line.strip())
        pass

import codecs
with codecs.open('.\\gitcommand.txt','r','utf-8') as f:
    for line in f.readlines()[:10]:
        #print(line.strip())
        pass

with open('.\\gitcommand.txt','a') as f:
    #f.write(u'世界'.encode('utf-8'))
    pass

import os
print os.name
#print os.uname()
#print os.environ
print os.getenv('PATH')
print os.path.abspath('.')
#print os.path.join(os.path.abspath('.'),'iotest.py')
#print os.path.split(os.path.join(os.path.abspath('.'),'iotest.py'))
#print os.path.splitext(os.path.join(os.path.abspath('.'),'iotest.py'))
#print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

#print os.listdir('D:\\My Documents')
#print [name.decode('gbk') for name in os.listdir('D:\\My Documents')]
for line in [name.decode('gbk') for name in os.listdir('D:\\My Documents')]:
    #print line
    pass


import os
import re
def search(path,name):
    for node in os.listdir(path):
        if os.path.isfile(os.path.join(path,node)):
            if re.search(name,node):
                print os.path.join(path,node)
        elif os.path.isdir(os.path.join(path,node)):
            if re.search(name,node):
                print os.path.join(path,node)
            search(os.path.join(path,node),name)
        
#search('.','test')
#search('D:\\fusion docs','Australian')
#search('D:\\My Documents',u'运动'.encode('gbk'))
#search('D:\\My Documents',u'数据'.encode('gbk'))

try:
    import cPickle as pickle 
    print 'Use cPickle'
except ImportError:
    print 'Use pickle'
    import pickle

f = open('dump.txt','wb')
d = dict(names='Bob',age=20,score=88)
pickle.dump(d,f)
f.close()

f = open('dump.txt','rb')
d = pickle.load(f)
f.close()
print d

import json
d = dict(name='Bob',age=20,score=88)
print json.dumps(d)
json_str = '{"age":20,"score":88,"name":"Bob"}'
print json.loads(json_str)

class Student(object):
    """docstring for Student"""
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
s = Student('Bob',20,88)
def student2dict(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score
    }
print (json.dumps(s,default=student2dict))
print(json.dumps(s,default=lambda obj:obj.__dict__))

def dict2student(d):
    return Student(d['name'],d['age'],d['score'])

s1 = json.loads((json.dumps(s,default=lambda obj:obj.__dict__)),object_hook=dict2student)
print s1.name
