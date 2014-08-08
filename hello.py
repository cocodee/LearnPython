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
print r'\\'
print '\\'

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
def power(x=10,n=2):
    s = 1
    while n > 0:
        n = n-1
        s = s*x
    return s
print power(5)
print power(5,3)
print power(n=3)

#error 
def add_end(L=[]):
    L.append('END')
    return L
print add_end()
print add_end()

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print add_end()
print add_end()

#var
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum+n*n
    return sum
print calc(1,2)
print calc(*[1,2])

def person(name,age,**kw):
    print 'name',name,' age',age,' other',kw
    print kw
    print kw.keys()

person('Bob',35)
person('Bob',35,**{'city':'Beijing'})
person('Bob',35,city='Beijing')
print person('Bob',35,job='Engineer',city='Beijing')

def func(a,b,c=0,*args,**kw):
    print 'a=',a,' b=',b,' c=',c,' args=',args,' kw=',kw

func(1,2)
func(1,2,c=3)
func(1,2,3)
func(1,2,3,'a','b')
func(1,2,3,'a','b',x=99)
func(*(1,2,3,4),x=99)
func(*[1,2,3,4],x=100)

#no tail recursion optimization
def fact(n):
    return fact_iter(1,1,n)
def fact_iter(product,count,max):
    if count>max:
        return product
    return fact_iter(product*count,count+1,max)
print fact(5)
#print fact(1000) # maximum recursion depth exceeded

#slice
L = ['Michael','Sarah','Tracy','Bob','Jack']
print L[0:3]#do not include the last one
print L[-2:-1]
print L[0:-2]
L = range(100)
print L[:10]
print L[-10:]
print L[:10:2]
print L[::5]
print (0,1,2,3,4,5)[:3]
print 'ABCDEFG'[:3]
print 'ABCDEFG'[::2]

d = {'a':1,'b':2,'c':3}
for key in d:
    print key
for value in d.itervalues():
    print value
for k,v in d.iteritems():
    print k,v

for ch in 'ABC':
    print ch

from collections import Iterable
print isinstance('abc',Iterable)
print isinstance([1,2,3],Iterable)
print isinstance(123,Iterable)

for i,value in enumerate(['A','B','C']):
    print i,value

for x,y in [(1,1),(2,4),(3,9)]:
    print x,y

#range
print range(1,11)
print [x*x for x in range(1,11)]
print [[x,x] for x in range(1,11)]
print [m+n for m in 'ABC' for n in 'XYZ']
print [x*x for x in range(1,11) if x%2==0 and x!=6]

import os
print [d for d in os.listdir('.')]
d = {'x':'A','y':'B','z':'C'}
print [k+'='+v for k,v in d.iteritems()]

L =['Hello','World','IBM','Apple']
print [s.lower() for s in L]
L = ['Hello','World',18,'Apple',None]
print [s.lower() for s in L if isinstance(s,str)]

#generator
g = (x*x for x in range(10))
for n in g:
    print n

def fab(max):
    n,a,b = 0,0,1
    while n<max:
        yield b
        a,b = b,a+b
        n = n+1
for n in fab(6):
    print n


def odd():
    print 'step 1'
    yield 1
    print 'step 2'
    yield 2
    print 'step 3'
    yield 3

for n in odd():
    print n

#lambda
def str2int(s):
    def fn(x,y):
        return x*10+y
    return reduce(fn,map(int,s))
print [str2int('123')]
print ['123']

def str2int2(s):
    return reduce(lambda x,y:x*10+y, map(int,s))
print [str2int2('123')]

def cmp_ignore_case(s1,s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1<u2:
        return -1
    if u1>u2:
        return 1
    return 0
print sorted(['about','bob','Zoo','Credit'],cmp_ignore_case)

def my_map(func,args):
    result = []
    for arg in args:
        result.append(func(arg))
    return result

def str2int3(s):
    return reduce(lambda x,y:x*10+y, my_map(int,s))
print [str2int3('123')]

#lambda
print map(lambda x:x*x,range(1,10))

#decarator
import functools
def log(text=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print '%s %s():'%(text,func.__name__)
            result = func(*args,**kw)
            print 'end call'
            return result
        return wrapper
    return decorator

@log('execute')
def now():
    print '2014'

now()

print now.__name__

@log()
def future():
    print '2015'

future()

#partial
import functools
int2 = functools.partial(int,base=2)
print int2('1000000')
print int2('1010101')
print int2('1010101',base=10)

#module
import sys
print sys.path
sys.path.append('D:\My_Projects\PYLearn')
print sys.path

#from __future__ import unicode_literals
#from __future__ import division

