#python3

#use Array to realize Queue

from Array import Array

class FullError(Exception):
    pass

class ArrayQueue(object):
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.array = Array(maxsize)
        self.head = 0
        self.tail = 0
    
    def push(self,value):
        if len(self) >= self.maxsize:
            raise FullError("Queue full")
        self.array._items[self.head % self.maxsize] = value
        self.head += 1
    
    def pop(self):
        value = self.array._items[self.tail & self.maxsize]
        self.tail += 1
        return value

    def __len__(self):
        return self.head - self.tail
    
if __name__ == "__main__":
    q1 = ArrayQueue(5)
    q1.push(1)
    q1.push(1)
    q1.push(199)
    q1.push(2)
    print(q1.pop())
    print(q1.array._items)
