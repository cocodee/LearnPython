#hello.py 
#-*- coding:utf-8 -*-
print 'hello,world'
print u'中文'
print '中文'.decode('utf-8') 
print 'Hello,%s' % 'world'
print 'Hi,%s, you have $%d.'%('Klein',100000000)
print 'Hi,%s'%u'云燕'
print 'growth rate:%d%%'%7
print 'Number %x'%0xffe8

#list
classmates = ['Michael','Bob','Tracy']
print classmates
print len(classmates)
print classmates[0]
print classmates[-1]
#print classmates.append('Adam') will not work
classmates.append('Adam')
print classmates
classmates.insert(1,'Jack')
print classmates
classmates.pop()
print classmates
classmates.pop(2)
print classmates
classmates[1]='Sarah'
print classmates