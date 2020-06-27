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

    def addNodeAfter(self,key,data):
        curr = self.head
        if curr.next is None and curr.data == key:
            self.append(data)
            return
        elif curr.data == key:
            newNode = Node(data)
            nxt = curr.next
            curr.next = newNode
            newNode.next = nxt
            newNode.prev = curr
            nxt.prev = newNode
            return
        curr = curr.next
    
    def addNodeBefore(self,key,data):
        curr = self.head
        while curr:
            if curr.prev is None and curr.data == key:
                self.prepend(data)
                return
            elif curr.data == key:
                newNode = Node(data)
                prev = curr.prev
                prev.next = newNode
                newNode.next = curr
                newNode.prev = prev
                curr.prev = newNode
                return
            curr = curr.next

    def deleteNode(self,key):
        curr = self.head
        while curr:
            if curr.data == key and curr == self.head:
                #only one node in the linkedlist
                if not curr.next:
                    curr = None
                    self.head = None
                    return

                #if the key is the head node in the linkedlist
                else:
                    nxt = curr.next
                    curr.next = None
                    nxt.prev = None
                    curr = None
                    self.head = nxt
                    return
                
            #not the head node
            elif curr.data == key:
                if curr.next:
                    nxt = curr.next
                    prev = curr.prev
                    prev.next = nxt
                    nxt.prev = prev
                    curr.next = None
                    curr.prev = None
                    curr = None

                #end node of the linkedlist
                else:
                    prev = curr.prev
                    prev.next = None
                    curr.prev = None
                    curr = None
                    return

            curr = curr.next



def op1():
    llist = DoubleLinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(4)
    llist.prepend(5)
    llist.printList()


if __name__ == "__main__":
    op1()