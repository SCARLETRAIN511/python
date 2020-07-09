#use super function for the implemention of inheritence

class Vehicle:
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model

    def printDetails(self):
        print("Manufacturer:", self.make)
        print("Color:", self.color)
        print("Model:", self.model)


class Car(Vehicle):
    def __init__(self, make, color, model, doors):
        super().__init__(make, color, model)
        self.doors = doors

    def printCarDetails(self):
        self.printDetails()
        print("Name:", self.doors)


obj1 = Car("Suzuki", "Grey", "2015", 4)
obj1.printCarDetails()



#without the super() function

class Plane:
    def __init__(self, make, color, model):
        self.make = make
        self.color = color
        self.model = model

    def printDetails(self):
        print("Manufacturer:", self.make)
        print("Color:", self.color)
        print("Model:", self.model)


class Drone(Plane):
    def __init__(self, make, color, model, doors):
        Plane.__init__(self,make, color, model)
        self.doors = doors

    def printCarDetails(self):
        self.printDetails()
        print("Name:", self.doors)


dji = Drone("Dji","white","phantom",6)
print(dji.make)
