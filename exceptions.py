#exceptions.py 
#-*- coding:utf-8 -*-

#exceptions
try:
    print u'try。。。'
    r = 10/0
    print 'result:',r
except ZeroDivisionError,e:
    print 'except:',e
finally:
    print 'finally...'
print 'END'

try:
    print u'try。。。'
    r = 10/int('1')
    print 'result:',r
except ValueError,e:
    print 'ValueError:',e
except ZeroDivisionError,e:
    print 'ZeroDivisionError:',e
else:
    print 'no error!'
finally:
    print 'finally...'
print 'END'

def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s)*2
def main():
    try:
        bar('0')
    except StandardError,e:
        print 'Error!'
    finally:
        print 'finally...'
main()

def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s)*2
def main():
    bar('0')
#main()


import logging

def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s)*2
def main():
    try:
        bar('0')
    except StandardError,e:
        logging.exception(e)
    finally:
        print 'finally...'

main()
print 'END'

class FooError(StandardError):
    """docstring for FooError"""
    pass

def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s'%s)
    return 10/n
#foo(0)

def foo(s):
    n = int(s)
    return 10/n
def bar(s):
    try:
        return foo(s)*2
    except StandardError,e:
        print 'Log error and raise'
        raise
def main():
    bar('0')
#main()

import logging
import pdb
logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
#pdb.set_trace()
logging.info('n=%d'%n)
#print 10/n

#python -m pdb exceptions.py 
#l,n,p,q

