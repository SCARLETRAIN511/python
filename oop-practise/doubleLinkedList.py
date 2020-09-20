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
                    return

                #end node of the linkedlist
                else:
                    prev = curr.prev
                    prev.next = None
                    curr.prev = None
                    curr = None
                    return

            curr = curr.next
    
    def reverse(self):
        temp = None
        curr = self.head
        while curr:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            curr = curr.prev
        if temp:
            self.head = temp.prev

    def removeDuplicates(self):
        curr = self.head
        seen = dict()
        while curr:
            if curr.data not in seen:
                seen[curr.data] = 1
                curr = curr.next
            else:
                nxt = curr.next
                #also can use the method above using the node.data
                #self.deleteNode(curr.data)
                self.delete_node(curr)
                curr = nxt

    def delete_node(self, node):
        cur = self.head
        while cur:
            if cur == node and cur == self.head:
            # Case 1:
                if not cur.next:
                    cur = None 
                    self.head = None
                    return

            # Case 2:
                else:
                    nxt = cur.next
                    cur.next = None 
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return 

            elif cur == node:
                # Case 3:
                if cur.next:
                    nxt = cur.next 
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None 
                    cur.prev = None
                    cur = None
                    return

        # Case 4:
                else:
                    prev = cur.prev 
                    prev.next = None 
                    cur.prev = None 
                    cur = None 
                    return 
            cur = cur.next

    def pairSum(self,sumValue):
        pairs = []
        p = self.head
        q = None
        while p:
            q = p.next
            while q:
                if (p.data + q.data == sumValue):
                    pairs.append("(" + str(p.data) +" " + str(q.data) + ")")
                q = q.next
            p = p.next
        return pairs



def op1():
    llist = DoubleLinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(4)
    llist.prepend(5)
    llist.reverse()
    llist.append(5)
    llist.printList()
    llist.removeDuplicates()
    llist.printList()
    print(llist.pairSum(6))

if __name__ == "__main__":
    op1()