#python3

#make Stack
#last in first out


from collections import deque
from doubleLinkedList import DoubleLinkedList

class Deque(DoubleLinkedList):

    def pop(self):
        if len(self) == 0:
            raise Exception("Error")
        tailnode =self.tailNode()
        value = tailnode.value
        self.remove(tailnode)
        return value
    
    def popleft(self):
        if len(self) == 0:
            raise Exception("Error")
        headnode = self.headNode()
        value = headnode.value
        self.remove(headnode)
        return value
    

class Stack():
    def __init__(self):
        self.deque = deque()
    
    def push(self,value):
        return self.deque.append(value)
    
    def pop(self):
        return self.deque.pop()
    
    def __len__(self):
        return len(self.deque)
    
    def isEmpty(self):
        return len(self) == 0


if __name__ == "__main__":
    d1 = Deque()
    d1.append(1)
    s1 = Stack()
    s1.push(1)
    s1.push(3)
    print(len(s1))
    s2 = Stack()
    print(s1.pop())#should print(3)
    print(s1.isEmpty())