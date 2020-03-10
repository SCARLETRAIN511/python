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