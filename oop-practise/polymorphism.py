#practise about polymorphism
#both classes have the method getArea(), but they will return different areas
from abc import ABC, abstractmethod

class Rectangle:
    def __init__(self,width = 0, height = 0):
        self.width = width
        self.height = height
        self.sides = 4
    
    def getArea(self):
        return self.width * self.height


class Circle:
    def __init__(self,radius = 0):
        self.radius = radius
        self.sides = 0
    
    def getArea(self):
        return self.radius ** 2 * 3.142


#shapes = [Rectangle(6,10),Circle(7)]
#print(shapes[0].sides)

class Shape():
    def __init__(self):
        self.sides = 0
    
    def getArea(self):
        pass

class Rectangle(Shape):
    def __init__(self,width = 0, height = 0):
        self.width = width
        self.height = height

    #method overriding
    def getArea(self):
        return (self.width * self.height)

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius 
        self.sides = 0

    #method overriding
    def getArea(self):
        return self.radius ** 2 * 3.14 
    #the method overriding is the top priority in the child class


#operator overriding
class Com:
    def __init__(self,real = 0, img = 0):
        self.real = real
        self.img = img
    
    #this is to replace the + operator
    def __add__(self,other):
        temp = Com(self.real + other.real, self.img + other.img)
        return temp

    #this is to replace the - operator
    def __sub__(self,other):
        temp = Com(self.real - other.real, self.img -other.img)
        return temp
    

def classOp1():
    obj1 = Com(3,2)#this is actually 3+2i
    obj2 = Com(1,3)#this is actually 1+3i
    obj3 = obj1 + obj2
    obj4 = obj1 - obj2
    print(obj3.real)


#abstract base class
#class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass


#class Square(Shape):
    def __init__(self,length):
        self.length = length
        
    def area(self):
        return self.length ** 2
    
    def perimeter(self):
        return 4 * self.length

#mostly, the parent class can act as a template for the child class, thus we should import the ABC and abstract class method
class Car(ABC):
    @abstractmethod
    def getSpeed(self):
        pass

    @abstractmethod
    def getDistance(self):
        pass

class Benz(Car):
    def __init__(self,speed,distance):
        self.distance = distance
        self.speed = speed

    def getDistance(self):
        return self.distance
    
    def getSpeed(self):
        return self.speed


def classOp2():
    Ecalss =Benz(120,30000)
    print(Ecalss.getDistance())


if __name__ == "__main__":
    classOp2()