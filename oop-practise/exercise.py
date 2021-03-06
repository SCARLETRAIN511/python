class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        return self.x**2 + self.y**2 + self.z**2

p1 = Point(1,2,4)


class Student:
    def __init__(self,phy,chem,bio):
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def totalObtained(self):
        return (self.phy + self.chem + self.bio)

    def Percentage(self):
        return self.totalObtained()/300*100


class Calculator():
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num2 - self.num1

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num2/self.num1


class User:
    def __init__(self,userName = None, password = None):
        self.__userName = userName
        self.__password = password
    
    def login(self,userName,password):
        if (self.__userName.lower() == userName.lower()) and self.__password == password:
            print("Access granted congradulations user %s, please refresh" %userName)
        else:
            print("invalid name or password")

Helen = User('jt2418',652117)
Helen.login('jt2418',652117)
