class Employee():
    def __init__(self,id,age,salary,department):
        self.id = id
        self.age = age
        self.salary = salary
        self.department = department

Steve = Employee(1,19,19000,'electrics')

print(Steve.id)