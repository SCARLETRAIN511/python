#data structure
#linear structure


#FIFO first in first out
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


##for stack, top and base, delete and add happen at one end/ LIFO structure, last in first out
##we can either use left or right as the top of the stack
class Stack():
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):#return the last item in the stack
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

#无序表
class Linked_list(object):
    def __init__(self):
        self.head=None
    def add(self,item):
        #添加必须添加在表头 顺序不能变
        temp=Node(item)
        temp.setNext(self.head)
        self.head=temp

    def size(self):
        #当前节点指向表头
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
        #如果是表头，删除表头，指向第二个节点
        if previous == None:
            self.head = current.getNext
        #另一种情况，删除表中间的节点
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

#有序表
#表头是最小的数
#与链表实现一样

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
        while checking != None and not found and not stop:
            if checking == item:
                found = True
            else:
                if checking.getData > item:
                    stop = True
                else:
                    checking = checking.getNext()
        return found

    #from the start, find the first one bigger than the number insert
    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
            
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

#can either add or delete at the start or the end
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
    o1 = OrderedList()
    o1.add(1)
    o1.add(10)
    o1.add(5)
    t = o1.head
    list1 = []
    #print the linked list
    while t!= None:
        print(t.getData())
        list1.append(t.getData())
        t = t.next
    print(list1)