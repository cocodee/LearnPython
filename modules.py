#modules.py
#-*- coding:utf-8 -*-
import base64

def safe_b64decode(string):
    mod = len(string)%4
    if mod == 0:
        return base64.b64decode(string)
    else:
        for i in range(4-mod):
            string = string+'='
        return base64.b64decode(string)
print base64.b64decode('YWJjZA==')
print safe_b64decode('YWJjZA')
print safe_b64decode('YWJjZA==')

#struct
s = '\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
import struct
print struct.unpack('<ccIIIIIIHH',s)

#hashlib
import hashlib
md5=hashlib.md5()
md5.update('how to use md5 in python hashlib?')
print md5.hexdigest()

md5=hashlib.md5()
md5.update('how to use md5 in ')
md5.update('python hashlib?')
print md5.hexdigest()

sha1 = hashlib.sha1()
sha1.update('how to use md5 in python hashlib?')
print sha1.hexdigest()

def get_md5(content):
    md5=hashlib.md5()
    md5.update(content)
    return md5.hexdigest()

db = {}
def register(username,password):
    db[username] = get_md5(password+username+'ALLINOROUT')

def login(username,password):
    md5=get_md5(password+username+'ALLINOROUT')
    print md5
    if (db[username]==md5):
        return True
    else:
        return False

register('cocodee','82212806')
print login('cocodee','82212806')
print login('cocodee','8221280')

#xml
from xml.parsers.expat import ParserCreate
class DefaultSaxHandler(object):
    def __init__(self):
        self.weathers = []

    def start_element(self,name,attrs):
        #print('sax:start_element:%s,attrs:%s'%(name,str(attrs)))
        if(name=='yweather:forecast'):
            self.weathers.append(attrs)

    def end_element(self,name):
        pass
        #print('sax:end_element:%s'%name)
    def char_data(self,text):
        pass
        #print('sax:char_data:%s'%text)
    def showWeather(self):
        print self.weathers

f = open('./beijingWeather.xml','r')
handler = DefaultSaxHandler()
parser = ParserCreate()
parser.returns_unicode = True
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(f.read())
handler.showWeather()
f.close()

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print('<%s>'%tag)
    def handle_endtag(self,tag):
        print('<%s>'%tag)
    def handle_startendtag(self,tag,attrs):
        print('<%s/>'%tag)
    def handle_data(self,data):
        print('data')
    def handle_comment(self,data):
        print('<!--  -->')
    def handle_entityref(self,name):
        print('&%s;'%name)
    def handle_charref(self,name):
        print('&#%s;'%name)
parser = MyHTMLParser()
print parser.feed('<html><head></head><body><p>Some <a href=\"#\">html</a> tutorial...<br>END</p></body></html>')