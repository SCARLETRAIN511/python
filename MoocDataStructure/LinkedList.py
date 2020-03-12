#python3

class Node(object):
    def __init__(self,value = None, next=None):
        self.value = value
        self.next = next

class LinkedList(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.root = Node()
        self.length = 0
        self.tailnode = None

    def __len__(self):
        return self.length
    
    def append(self,value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception("Full")
        node = Node(value)
        tailnode = self.tailnode
        if tailnode == None:
            self.root.next = node
        else:
            tailnode.next = node
        self.tailnode = node
        self.length += 1
    
    def appedleft(self,value):
        headnode = self.root.next
        node = Node(value)
        self.root.next = node
        node.next = headnode
        self.length += 1

    def iter_node(self):
        currentNode = self.root.next
        while currentNode is not self.tailnode:
            yield currentNode
            currentNode = currentNode.next
        yield currentNode
    
    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def remove(self, value):
        prenode = self.root
        currnode = self.root.next
        while currnode.next is not None:
            if currnode.value == value:
                prenode.next = currnode.next()
                del currnode
                self.length -= 1
                return
    def find(self, value):
        index = 0
        for node in self.iter_node():
            if node.value == value:
                return index
            index += 1
        return -1
    
    def popLeft(self):
        if self.root.next is None:
            raise Exception("Pop from empty linkedlist")
        headnode = self.root.next
        self.root.next = headnode.next
        self.length -= 1
        value = headnode.value
        del headnode
        return value
    
    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next = None
        self.length = 0
    
##append 与 appendleft 都是o[1]
##find 与remove 都是 o[n]
if __name__ == "__main__":
    
    def testLinkedList():
        ll = LinkedList()
        ll.append(9)
        ll.append(1)
        print(ll.length)
        ll.popLeft()
        print(ll.length)
        ll.append(1)
        ll.appedleft(1)
        print(ll.length)


    testLinkedList()