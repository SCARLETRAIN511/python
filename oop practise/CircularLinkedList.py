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

    def prepend(self,data):
        newNode = Node(data)
        curr = self.head
        newNode.next = self.head
        
        if not self.head:
            newNode.next = newNode
        else:
            while curr.next != self.head:
                curr = curr.next
            #form a circular linkedlist, make sure the end node.next is the head node
            curr.next = newNode
        self.head = newNode
        
    def remove(self,key):
        if self.head:
            if self.head.data == key:
                curr = self.head
                while curr.next != self.head:
                    curr = curr.next
                if self.head == self.head.next:
                    self.head = None
                else:
                    #form a circular linkedList, the end node of the linkedlist.next should be the headnode.next as the headnode is the key
                    curr.next = self.head.next
                    #after change the endnode.next, change the headnode to the next node in the linkedlist
                    self.head = self.head.next
            else:
                #if the headnode is not the key
                curr = self.head
                prev = None
                while curr.next != self.head:
                    prev = curr
                    curr = curr.next
                    if curr.data == key:
                        prev.next = curr.next
                        curr = curr.next
        #otherwise the linkedlist has no node inside
        else:
            return

    def getLength(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next
            if curr == self.head:
                break
        
        return count

    def splitHalf(self):
        size = self.getLength()
        if size == 0:
            return None
        if size == 1:
            return self.head
        
        #floor divide
        mid = size//2
        count = 0
        prev = None
        curr = self.head
        while count < mid and curr:
            prev = curr
            curr = curr.next
            count += 1
        #create the first half
        prev.next = self.head

        splitList = CircularLinkedList()
        while curr.next != self.head:
            splitList.append(curr.data)
            curr = curr.next
        #append the last node after exit the while loop
        splitList.append(curr.data)

        self.printList()
        splitList.printList()



def op1():
    llist = CircularLinkedList()
    llist.append(1)
    llist.append(2)
    llist.remove(1)
    llist.append(120)
    llist.append("Helo")
    llist.printList()
    print(llist.getLength())
    llist.splitHalf()

if __name__ == "__main__":
    op1()