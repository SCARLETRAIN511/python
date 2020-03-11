#python3

#双端链表

class Node(object):
    def __init__(self,value = None, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next
        
class DoubleLinkedList():
    #闭环
    def __init__(self, maxsize = None):
        self.maxsize = maxsize
        node = Node()
        node.next, node.prev = node, node
        self.root = node
        self.length = 0

    def __len__(self):
        return self.length

    def headNode(self):
        return self.root.next

    def tailNode(self):
        return self.root.prev


    def append(self, value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception("full")
        node = Node(value=value)
        tailnode = self.tailNode()
        tailnode.next = node
        node.prev = tailnode
        node.next = self.root

        #root指向最后一个数 形成闭环
        self.root.prev = node

        self.length += 1

    def appendleft(self,value):
        node = Node(value = value)

        if self.root.next is self.root:
            node.next = self.root
            node.prev = self.root
            self.root.next = node
            self.root.prev = node
        else:
            node.prev = self.root
            headnode = self.root.next
            node.next = headnode
            headnode.prev = node
            self.root.next = node

        self.length += 1

    def remove(self, node):
        if node is self.root:
            return
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1
        return node.value
    
    def iter_node(self):
        if self.root.next == self.root:
            return
        currnode = self.root.next
        while currnode.next is not self.root:
            yield currnode
            currnode = currnode.next
        yield currnode
        
    def __iter__(self):
        for node in self.iter_node():
            yield node.value
    
    def iter_node_reverse(self):
        if self.root.prev is self.node:
            return
        currnode = self.node.prev
        while currnode.prev is not self.root():
            yield currnode
            currnode = currnode.next
        yield currnode


def testDoubleLinkedList():
    dll = DoubleLinkedList()
    print(dll.length)
    dll.append(1)
    dll.append(2)
    dll.appendleft(19)
    headnode = dll.headNode()
    dll.remove(headnode)
    last = dll.tailNode()
    print([node.value for node in dll.iter_node()])

    print(dll.remove(last))
    print([node.value for node in dll.iter_node()])

testDoubleLinkedList()


            

    

