#implemention about inheritence
class Vehicle:
    def setTopSpeed(self,speed):
        self.TopSpeed = speed
        print("Top speed is set to ", self.TopSpeed)

class Car(Vehicle):
    def openTrunk(self):
        print("Trunk is open")
    
class Hybrid(Car):
    def turnOnHybrid(self):
        print("Hybrid mode is no switched on")

class Truck(Vehicle):
    def drive(self):
        print("the truck is driving")


def classOp1():
    corolla = Car()  # creating an object of the Car class
    corolla.setTopSpeed(220)  # accessing methods from the parent class
    corolla.openTrunk()  # accessing method from its own class

    priusPrime = Hybrid()  # creating an object of the Prius class
    priusPrime.setTopSpeed(220)  # accessing methods from the parent class
    priusPrime.openTrunk()  # accessing method from the parent class
    priusPrime.turnOnHybrid()  # accessing method from the parent class

    scania = Truck()
    scania.setTopSpeed(20)
    scania.drive()



#implemention of multiple inheritence
#also hybrid inheritence
class Engine:
    def setPower(self,power):
        self.power = power

class CombustionEngine(Engine):
    def setTankCapacity(self,tankCapacity):
        self.tankCapacity = tankCapacity

class ElectricEngine(Engine):
    def setChargeCapacity(self, chargeCapacity):
        self.chargeCapacity = chargeCapacity

class HybridEngine(CombustionEngine,ElectricEngine):
    def printDetails(self):
        print(self.tankCapacity)
        print(self.chargeCapacity)
        print(self.power)


def classOp2():
    tesla1 = HybridEngine()
    tesla1.setPower("230hp")
    tesla1.setChargeCapacity(199)
    tesla1.setTankCapacity(200)
    tesla1.printDetails()


if __name__ == "__main__":
    classOp2()