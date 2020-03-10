from ds1 import Queue
import random


#using s as the unit of time here
class Printer:
    def __init__(self,ppm):
        self.pagerate = ppm#speed of printing
        self.currentTask = None
        self.timeRemaining = 0#timer for the task

    def tick(self):#print for 1 sec here
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None
    
    #if busy or not of the printer
    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages()*60/(self.pagerate)#get the time remaining for the task


class Task:
    def __init__(self,time):
        self.timestamp = time#generate the timestamp
        self.pages = random.randrange(1,21)#randomly generate the number of pages
    
    def getStamp(self):
        return self.timestamp
    
    def getPages(self):
        return self.pages
    
    def waitTime(self, currenttime):
        return currenttime - self.timestamp

#randomly generate the task for printing
def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

#start the simulation. PagesPerMinute set the rate of the printer
def simulation(numSeconds, pagesPerMinute):

    labprinter = Printer(pagesPerMinute)#initate the printer
    printQueue = Queue()#get the buffer area
    waitingtimes = []
    
    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)
        
        labprinter.tick()
    averageWait = sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks reamining"%(averageWait, printQueue.size()))


    
if __name__ == "__main__":
    for i in range(19):
        simulation(3600,5)