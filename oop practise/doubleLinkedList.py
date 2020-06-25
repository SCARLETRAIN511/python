#double linkedlist

class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
        self.prev = None
    

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        if not self.head:
            newNode = Node(data)
            newNode.prev = None
            self.head = newNode
        else:
            newNode = Node(data)
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newNode
            newNode.prev = curr
            newNode.next = None
    