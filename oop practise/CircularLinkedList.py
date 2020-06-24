class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        if not self.head:
            self.head = Node(data)
            #this is a circular linkedList
            self.head.next = self.head
        else:
            newNode = Node(data)
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = newNode
            newNode.next = self.head
    
    def printList(self):
        curr = self.head
        listValue = []
        while curr:
            listValue.append(curr.data)
            curr = curr.next
            if curr == self.head:
                break
        print(listValue)


def op1():
    llist = CircularLinkedList()
    llist.append(1)
    llist.append(2)

    llist.printList()

if __name__ == "__main__":
    op1()