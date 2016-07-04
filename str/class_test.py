#encoding:utf-8
__metaclass__ = type

class Person:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def greet(self):
        print "Hello,World! I'm %s." % self.name

foo = Person()
bar = Person()

foo.setName('Luke Skywalker')
bar.setName('Anakin Skywalker')

foo.greet()
bar.greet()

class Class:
    def method(self):
        print('I have a self!')

def function():
    print("I don't...")

instance = Class()
instance.method()

instance.method = function
instance.method()

class Filter:
    def init(self):
        self.blocked = []
    def filter(self,sequence):
        return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter):
    def init(self):
        self.blocked = ['SPAM']

issubclass(SPAMFilter,Filter)

issubclass(Filter,SPAMFilter)

class Calculator:
    def calculate(self,expression):
        self.value = eval(expression)

class Talker:
    def talk(self):
        print 'Hi,my value is ',self.value
class TalkingCalculator(Calculator,Talker):
    pass

tc = TalkingCalculator()
tc.calculate('1+2*5')
tc.talk()

class Person:
    def __init__(self,name): #__init__ 方法在类的一个对象建立时，马上运行。这个方法可以用来对你的对象做一些初始化。
        self.name=name
    def sayHi(self):
        print 'Hello,how are you?',self.name

p = Person('Mdgsg')
print p
p.sayHi()

def in_fridge():
    try:
        count = fridge[wanted_food]
    except KeyError:
        count = 0
    return count

    fridge= {'apples':10,'orages':3,'milk':2}
    wanted_food = 'apples'
    in_fridge()
    wanted_food = 'oranges'
    in_fridge()
    wanted_food = 'milk'
    in_fridge()

    











