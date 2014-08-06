#hello.py 
#-*- coding:utf-8 -*-
print 'hello,world'
print u'中文'
print '中文'#Wrong encoding from utf-8 to unicode
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
L = ['Apple',123,True]
print L
s = ['python','java',['asp','php'],'scheme']
print s
print len(s)

#tuple
classmates = ('Michael','Bob','Tracy')
print classmates
t = (1,)
print t
t = ('a','b',['A','B'])
t[2][1] = 'C'
print t
a = 'abc'
t = (a,)
print t
a = 'def'
print t
t = (a,)
print t

#if
age = 20
if age >= 18:
    print 'Your age is ',age
    print 'adult'
else:
    print 'Your age is ',age
    print 'teenager'

age = 7
if age >= 18:
    print 'Your age is ',age
    print 'adult'
elif age >= 6:
    print 'teenager'
else:
    print 'Your age is ',age
    print 'kid'

#loop
names = ['Michael','Bob','Tracy']
for name in names:
    print name

sum = 0
for x in range(101):
    sum = sum + x
print sum

sum = 0
n = 100
while n>0:
    sum = sum+n
    n = n-1
print sum

#birth = int(raw_input('birth: '))
birth = 2000
if birth > 2000:
    print u'00后'
elif birth <2000:
    print u'00前'
else:
    print u'你妹儿'

#dict
d = {'Michael' : 95, 'Bob' : 75, 'Tracy' : 85}
print d['Michael']
print 'Bob' in d
print d.get('Tomas')
print d.get('Tomas',-1)
d.pop('Michael')
print d.has_key('Michael')
print d.has_key('Bob')

#set
s = set((1,2,3,3))
print s
s.add(4)
print s
s.remove(4)
print s
s1 = set([1,2,3])
s2 = set([2,3,4])
print s1&s2
print s1-s2
print s1|s2
print s2-s1

a = ['c','b','a']
print a.sort()
print a
a = 'abc'
print a.replace('a','A')
print a

#function
print abs(-20)
print cmp(1,2),',',cmp(2,1),',',cmp(1,1)
print int(12.34)
print float('12.34')
print long('1000')
print unicode(100)
print bool(1)
print bool('')

myabs = abs
print myabs(-2000)

#def 
def my_abs(x):
    if x>= 0:
        return x
    else:
        return -x
print my_abs(-2000)
print my_abs(2000)

def nop():
    pass

nop
print my_abs('A')

def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print my_abs(-200)
#print my_abs('A')

import math
def move(x,y,step,angle=0):
    nx = x+step*math.cos(angle)
    ny = x+step*math.sin(angle)
    return nx,ny
x,y = move(100,100,60,math.pi/6)
print x,y
r = move(100,100,60,math.pi/6)
print r

#parameter
def power(x,n=2):
    s = 1
    while n > 0:
        n = n-1
        s = s*x
    return s
print power(5)
print power(5,3)


