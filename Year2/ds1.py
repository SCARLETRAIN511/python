#data structure


class Queue():
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

class Stack():
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

class Node:
    def __init__(self,initdata):
        self.data=initdata
        self.next=None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newdata):
        self.data=newdata
    def setNext(self,newnext):
        self.next=newnext


class Linked_list(object):
    def __init__(self):
        self.head=None
    def add(self,item):
        temp=Node(item)
        temp.setNext(self.head)
        self.head=temp

    def size(self):
        current=self.head
        count=0
        while current != None:
            count = count+1
            current = current.getNext()
        return count

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext
        else:
            previous.setNext(current.getNext())

    def search(self,data):
        checking = self.head
        while checking != None:
            if checking.getData() == data:
                return True
            checking = checking.getNext()
        return False

    def isEmpty(self):
        return self.head == None


class OrderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def size(self):
        current=self.head
        count=0
        while current != None:
            count = count+1
            current = current.getNext()
        return count

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext
        else:
            previous.setNext(current.getNext())

    def search(self,item):
        checking = self.head
        found = False
        stop = False
        while checking != None and not stop:
            if checking == item:
                found = True
            else:
                if checking.getData > item:
                    stop = True
                else:
                    checking = checking.getNext()
        return found

    def add(seld, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getNext() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
            
            temp = Node(item)
            if previous = None:
                temp.setNext(self.head)
                self.head = temp
            else:
                temp.setNext(current)
                previous.setNext(temp)


class Deque:
    def __init__(self):
        self.items = []
    def addFont(self,item):
        self.items.append(item)
    def addRear(self,item):
        self.items.insert(0,item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.items == []

    

if __name__ == "__main__":
    a = Deque()
    a.addFont(1)
    print(a.items)
    print(a.removeFront())