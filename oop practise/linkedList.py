class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
  
    def printList(self):
        node = self.head
        listItems = []
        while node:
            listItems.append(node.data)
            node = node.next
        
        print(listItems)


    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return

        lastNode = self.head
        while lastNode.next is not None:
            lastNode = lastNode.next
        
        lastNode.next = newNode

    def prepend(self,data):
        #insert the data at the head of the linkedlist
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insertAfterNode(self,prevNode,data):
        #insert the data right after the existing node in the linkedlist
        if not prevNode:
            print("The given node does not exist")
            return
        
        newNode = Node(data)
        newNode.next = prevNode.next
        prevNode.next = newNode
    
    def deleteNode(self,key):
        currentNode = self.head

        #the condition for the key is the headNode of the linkedlist
        if currentNode.data == key:
            self.head = currentNode.next
            currentNode = None
            return

        prev = None
        while currentNode and currentNode.data != key:
            prev = currentNode
            currentNode = currentNode.next    
        
        #the condition for the specified node is not in the linkedlist
        if not currentNode:
            return        
        
        prev.next = currentNode.next
        currentNode = None

    def deleteNodeByPos(self,pos):
        if pos<0:
            print("The position parameter is not valid")
            return

        currentNode = self.head
        index = 0

        if pos == 0:
            self.head = currentNode.next
            currentNode = None
            return

        prev = None
        while index != pos and currentNode.next:
            prev = currentNode
            currentNode = currentNode.next
            index += 1
        
        if not currentNode:
            prev.next = None
            return         

        prev.next = currentNode.next
        currentNode = None
    
    def getLength(self):
        currentNode = self.head
        length = 1
        while currentNode.next:
            length += 1
            currentNode = currentNode.next
        
        return length

    def getLengthRecursive(self,node):
        #the input variable should be the headnode of the linkedlist
        if node == None:
            return 0
        else:
            return 1+self.getLengthRecursive(node.next)

    def nodeExchange(self,key1,key2):
        #to check whether they are the same node
        if key1 == key2:
            return

        #use the iteration to locate the nodes that keys indicate
        prev1 = None
        currNode1 = self.head
        while currNode1 and currNode1.data != key1:
            prev1 = currNode1
            currNode1 = currNode1.next

        prev2 = None
        currNode2 = self.head
        while currNode2 and currNode2.data != key2:
            prev2 = currNode2
            currNode2 = currNode2.next
        
        #check whether both nodes exist or not
        if not currNode1 or not currNode2:
            return
        
        if prev1:
            prev1.next = currNode2
        #if the key corresponds to the head node
        else:
            self.head = currNode2

        if prev2:
            prev2.next = currNode1
        else:
            self.head = currNode1
        
        currNode1.next,currNode2.next = currNode2.next, currNode1.next

    #Reverse the linkedlist
    def reverse(self):
        prevNode = None
        currNode = self.head
        while currNode:
            nextNode = currNode.next
            #reverse the link
            currNode.next = prevNode

            #from the head to the end of the linkedlist, reverse the directions of links
            prevNode = currNode
            currNode = nextNode
            
        self.head = prevNode


def main():
    llist = LinkedList()
    llist.append("A")
    llist.append("B")
    llist.append("C")
    llist.append("D")
    llist.prepend("0")
    llist.prepend("K")
    llist.printList()
    #print(llist.getLength())
    #print(llist.getLengthRecursive(llist.head))
    llist.reverse()
    llist.printList()


if __name__ == "__main__":
    main()
    