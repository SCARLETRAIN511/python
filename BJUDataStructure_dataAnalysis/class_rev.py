
class Student(object):
    def __init__(self,x,y):
        self.__x=x
        self.__y=y
    def print_info(self):
        print("%s has score: %s" % (self.__x, self.__y))
    
    def edit_info(self,x,y):
        self.__x=x
        self.__y=y

    def get_info(self):
        #return a tuple
        return self.__x,self.__y

class Badstudent(Student):
    pass


class Employee:
    empcount=0

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empcount+=1
    
    def display(self):
        print("Name is :",self.name)
        print("the salary is:",self.salary)
    
    def displayCount(self):
        print("the total number in this company is %d" %Employee.empcount)

class Boss(Employee):
    def __init__(self,name,salary,year):
        Employee.__init__(self,name,salary)
        self.year=year
    
    def print_year(self):
        print("the year is %d" %self.year)

    
def runTwice(animal):
    animal.print_info()
    animal.print_info()


def firstLambada():
    add = lambda x:x**2
    print(add(2))

def findPrime(number=10):
    for n in range(2, number+1):
        for x in range(2, number+1):
            if n % x == 0:
                print(n, 'equals', x, '*', n / x)
                break
        else:
        # loop fell through without finding a factor
            print(n, 'is a prime number')

def fib(n):
    if n<2:
        return n
    return fib(n-1) + fib(n-2)

def main1():
    print([fib(n) for n in range(10)])

if __name__ == "__main__":
    emp1=Employee('tjx',50000)
    emp1.displayCount()
    boss1=Boss('DB',100000,2019)
    boss1.print_year()