#class of object relations

class Country:
    def __init__(self,name = None,population = 0):
        self.name = name
        self.population = population

    def printDetails(self):
        print("Contry nams is %s" %self.name)
        print("It has popution %d ." %self.population)
    

class Person:
    def __init__(self, name, country):
        self.name = name
        self.country = country
    
    def printDetails(self):
        print("Person Name: %s ." %self.name)
        self.country.printDetails()


def classOp():
    c = Country("Wales",150000)
    p1 = Person("Helen", c)
    p1.printDetails()

#example2
class Engine:
    def __init__(self,capacity):
        self.capacity = capacity

    def printDetails(self):
        print("Engine details:",self.capacity)

class Tires:
    def __init__(self,tires = 0):
        self.tires = tires

    def printDetials(self):
        print("Number of tires %d" %self.tires)

class Doors:
    def __init__(self,doors = 0):
        self.doors = doors

    def printDetails(self):
        print("Number of doors: %d" %self.doors)


class Car:
    def __init__(self,eng,tr,dr,color):
        self.eobj = Engine(eng)
        self.tobj = Tires(tr)
        self.dobj = Doors(dr)
        self.color = color
    
    def printDetails(self):
        self.eobj.printDetails()
        self.tobj.printDetials()
        self.dobj.printDetails()
        print("Car color is %s" %self.color)


def classOp2():
    car = Car(1500,4,4,"Black")
    car.printDetails()


if __name__ == "__main__":
    classOp()
    classOp2()
        