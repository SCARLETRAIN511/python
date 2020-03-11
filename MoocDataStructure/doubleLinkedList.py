#python3

#双端链表

class Node(object):
    def __init__(self,value = None, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next
        
class CircularLinkedList():
    