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

    #this method is to merge 2 sorted linkedlist together to form still a sorted linkedlist
    def mergeSorted(self,llist):
        p = self.head
        q = llist.head
        s = None
        
        if not p:
            return q
        if not q:
            return p
        
        if p and q:
            if p.data < q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            newHead = s
        
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q;
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p
        return newHead

    def removeDuplicate(self):
        curr = self.head
        prev = None
        dup_values = dict()

        while curr:
            if curr.data in dup_values:
                prev.next = curr.next
                curr = None
            else:
                dup_values[curr.data] = 1
                prev = curr
            
            curr = prev.next

    def printNthfromLast(self,n):
        totalLength = self.getLength()

        curr = self.head
        while curr:
            if totalLength == n:
                print(curr.data)
                return curr.data
            totalLength -= 1
            curr = curr.next
        if curr is None:
            return
    
    #use the iteration to calculate the number of occurences
    def countOccurence(self,data):
        count = 0
        currentNode = self.head
        while currentNode:
            if currentNode.data == data:
                count += 1
            currentNode = currentNode.next
        return count

    #self.head should be the inital value for the node parameter here
    def countOccurenceRecur(self,node,data):
        if not node:
            return 0   
        if node.data == data:
            return 1 + self.countOccurenceRecur(node.next,data)
        else:
            return self.countOccurenceRecur(node.next,data)

    def rotate(self,k):
        if self.head and self.head.next:
            p = self.head
            q = self.head
            prev = None
            count = 0
            while p and count < k:
                prev = p
                p = q.next
                q = q.next
                count += 1
            p = prev
            while q:
                prev = q
                q = q.next
            q = prev
            q.next = self.head
            self.head = p.next
            p.next = None
    
    def isPalindrome(self):
        p = self.head
        s = []
        while p:
            s.append(p.data)
            p = p.next
        p = self.head
        while p:
            data = s.pop()
            if p.data != data:
                return False
            p = p.next
        return True

    def isPalindrome2(self):
        s = ""
        p = self.head
        while p:
            s += p.data
            p = p.next
        return s == s[::-1]

    #use 2 pointers
    def isPalindrome2Pointers(self):
        if self.head:
            p = self.head
            q = self.head
            prev = []

            i = 0
            while q:
                prev.append(q)
                q = q.next
                i += 1
            q = prev[i-1]
            count = 1

            while count<= i//2 + 1:
                if prev[-count].data != p.data:
                    return False
                p = p.next
                count += 1
            return True
        else:
            return True
        
    def movTailToHead(self):
        curr = self.head
        prev = None
        while curr.next:
            prev = curr
            curr = curr.next
            
        curr.next = self.head
        self.head = curr
        prev.next = None

    def sum2LinkedList(self,llist):
        curr1 = self.head
        curr2 = llist.head
        count1 = 0
        count2 = 0
        num1 = 0
        num2 = 0

        while curr1:
            num1 += curr1.data*10**(count1)
            curr1 = curr1.next
            count1 += 1

        while curr2:
            num2 += curr2.data*10**(count2)
            curr2 = curr2.next
            count2 += 1
        
        #calculate the number after the operation
        numSum = list(str(num1 + num2))
        l3 = LinkedList()
        for i in numSum:
            l3.append(i)
        l3.reverse()

        
        
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
    llist.printList()    
    llist.movTailToHead()
    llist.printList()

def op1():
    l1 = LinkedList()
    l1.append(1)
    l1.append(2)
    l1.append(3)

    l2 = LinkedList()
    l2.append(4)
    l2.append(5)
    l2.append(6)

    print(l1.sum2LinkedList(l2))


if __name__ == "__main__":
    op1()
    