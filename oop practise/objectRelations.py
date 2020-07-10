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


c = Country("Wales",150000)
p1 = Person("Helen", c)
p1.printDetails()
        