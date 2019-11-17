class MyNthClass(object):
    def __init__(self,name,position):
        self.name=name
        self.position=position
    
    def move(self,length):
        self.position+=length

#inheritence
class Tjx(MyNthClass):
    def __init__(self, name, position,age):
        MyNthClass.__init__(self,name,position)
        self.age=age

p1=Tjx('Tjx',4,19)
p1.move(5)
print(p1.position)