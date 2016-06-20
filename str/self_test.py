#encoding:utf-8
__author__ = 'zhen'

class Test:
    def test_self(self):
        print(self) #self代表的是类的实例，而非类
        print(self.__class__) #self.class 指向类
        print(self.__dict__)


class Test1(Test):
    def test1_self(self):
        print(self)
        print(self.__class__)

t = Test()
t.test_self()

t1 = Test1()
t1.test_self()
t1.test1_self()

class Desc:
    def __get__(self, instance, owner):
        print('self in Desc: %s ' % self)
        print(self,instance,owner)

class Test2:
    x = Desc()
    def prt(self):
        print('self in Test2: %s' % self)
t2 = Test2()
t2.prt()
t2.x



















