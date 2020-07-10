#challenge exercies

class Shape:
    def __init__(self,name):
        self.name = name
    
    def getName(self):
        return self.name
    

class Xshape(Shape):
    def __init__(self,name):
        super.__init__(name)
    
    def getName(self):
        return (super().getName() + ", " +self.name)

    
#challenge2 
class Animal:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound
    
    def Animal_details(self):
        print(self.name)
        print(self.sound)


class Dog(Animal):
    def __init__(self, name, sound,family):
        super().__init__(name, sound)
        self.family = family
    
    def Animal_details(self):
        print(self.family)
        return super().Animal_details()
        


class Sheep(Animal):
    def __init__(self, name, sound, color):
        super().__init__(name, sound)
        self.color = color

    def Animal_details(self):
        print(self.color)
        return super().Animal_details()


def classOp():
    dog1 = Dog("Skr","Wof","Husky")
    sheep1 = Sheep("Dolly","Mea","white")
    dog1.Animal_details()
    sheep1.Animal_details()
    

if __name__ == "__main__":
    classOp()

    
