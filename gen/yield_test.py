#coding:utf-8:
def fab(max):
    n,a,b = 0,0,1
    while n < max:
        print b
        a,b = b,a+b
        n = n + 1
    
def fab1(max):    
    n,a,b = 0,0,1
    L = []
    while n < max:
        L.append(b)
        a,b = b,a+b
        n = n + 1
    return L


class Fab(object):
    def __init__(self,max):
        self.max = max
        self.n,self.a,self.b = 0,0,1
    
    def __iter__(self):
        return self
    
    def next(self):
        if self.n < self.max:
            r = self.b
            self.a,self.b = self.b,self.a+self.b
            self.n = self.n + 1
            return r
        raise StopIteration()
    
fab2 = Fab()
for n in fab2(5):
    print n
