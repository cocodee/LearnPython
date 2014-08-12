#coroutine.py 
#-*- coding:utf-8 -*-
import time
def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] consuming %s...'%n)
        time.sleep(1)
        r = '200 OK'
def produce(c):
    c.next()
    n = 0
    while n<5:
        n = n+1
        print('[PRODUCER] Producing %s...'%n)
        r = c.send(n)
        print('[PRODUCER] Consumer return:%s'%r)
    c.close()

if __name__=='__main__':
    c = consumer()
    produce(c)
    
'''
from gevent import monkey;monkey.patch_all()
import gevent
import urllib2
urllib2.install_opener(
    urllib2.build_opener(
        urllib2.ProxyHandler({'http':'cn-proxy.jp.oracle.com'})))

def f(url):
    print('Get:%s'%url)
    resp = urllib2.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.'%(len(data),url))

gevent.joinall([
    gevent.spawn(f,'https://www.python.org/'),
    gevent.spawn(f,'https://www.yahoo.com'),
    gevent.spawn(f,'https://github.com/')
    ])
'''
