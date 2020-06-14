#class variables are defined ouside the initializer and instance variables are defined inside the initializer

class Employee():
    #class variables
    Employeelist = []

    def __init__(self,id,age,salary=13000,department="mechanical"):
        #instance variables
        self.id = id
        self.age = age
        self.salary = salary
        self.department = department
        self.Employeelist.append(self.id)


Steve = Employee(1,19,19000,'electrics')

Mark = Employee(2,20,190000,'mechanical')


print(Mark.Employeelist)
print(Employee.Employeelist)