#python3
from LinkedList import LinkedList, Node


##queue FIFO
class FullError(Exception):
    pass

class EmptyError(Exception):
    pass

class Queue(object):
    def __init__(self,maxsize = None):
        self.maxsize = maxsize
        self._item_linked_list = LinkedList()
    
    def __len__(self):
        return len(self._item_linked_list)
    
    def push(self,value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise FullError("Queue full")
        return self._item_linked_list.append(value)
    
    def pop(self):
        if len(self) <= 0:
            raise EmptyError("Queue empty")
        raise self._item_linked_list.popLeft()

if __name__ == "__main__":
    q1 = Queue()
    q1.push(1)
    print(len(q1))

