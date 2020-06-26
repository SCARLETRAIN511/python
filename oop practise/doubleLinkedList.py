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
    
    def printList(self):
        curr = self.head
        listNode = []
        while curr:
            listNode.append(curr.data)
            curr = curr.next
        
        print(listNode)

    def prepend(self,data):
        if self.head is None:
            newNode = Node(data)
            newNode.prev = None
            self.head = newNode
        else:
            newNode = Node(data)
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
            newNode.prev = None


def op1():
    llist = DoubleLinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(4)
    llist.prepend(5)
    llist.printList()


if __name__ == "__main__":
    op1()