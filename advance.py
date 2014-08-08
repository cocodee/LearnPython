#advance.py 
#-*- coding:utf-8 -*-
class Student(object):
    __slots__ = ('age','__name','__score','sex','set_age','__birth')
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s:%s'%(self.__name,self.__score)

    def get_grade(self):
        if self.__score>=90:
            return 'A'
        elif self.__score>=60:
            return 'B'
        else:
            return 'C'
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def __get_score(self):
        return self.__score
    def __len__(self):
        return len(self.__name)
    @property
    def birth(self):
        return self.__birth;
    @birth.setter
    def birth(self,value):
        self.__birth = value

bart = Student('Bart Simpson',59)
lisa = Student('Lisa Simpson',87)
bart.print_score()
print bart.get_grade()
lisa.print_score()
print lisa.get_grade()
print lisa.get_name()
print lisa._Student__name
print lisa._Student__get_score()

print type(123)
print type('string')
print type(u'黄薇')
print type(None)

print type(abs)
print type(Student)
print type(lisa)

import types
print type('abc')==types.StringType
print type(u'abc')==types.UnicodeType
print type([])==types.ListType
print type(str)==types.TypeType
print type(Student)==types.TypeType

print isinstance('a',(str,unicode))
print isinstance(u'黄薇',(str,unicode))

print len(lisa)
print getattr(lisa,'__name',u'黄薇')

if hasattr(lisa,'get_name'):
    fn = getattr(lisa,'get_name')
    print fn()


def set_age(self,age):
    self.age = age

from types import MethodType
s = Student('hw',90)
s.set_age = MethodType(set_age,s,Student)
s.set_age(25)
print s.age
print s.get_name()

def set_sex(self,sex):
    self.sex = sex

Student.set_sex = MethodType(set_sex,None,Student)
s.set_sex('female')
print s.sex
lisa.set_sex('female')
print lisa.sex
lisa.birth = '1995'
print lisa.birth

#multi-inheritence,mixin
#__str__
#__repr__
#__iter__
#__getitem__
#__getattr__
#__call__

#meta class
def fn(self,name='world'):
    print('Hello,%s.'% name)

Hello = type('Hello',(object,),{'hello':fn})

h = Hello()
h.hello()

class ListMetaclass(type):
    def __new__(cls,name,bases,attrs):
        attrs['add'] = lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)
class MyList(list):
    __metaclass__ = ListMetaclass

L = MyList()
L.add(1)
print L

#class attributes
class Student(object):
    name = 'Student'

s = Student()
print s.name

s.name = 'Lisa'
print s.name
print(Student.name)
del s.name
print(s.name)