#Implemention of queue

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self,data):
        self.items.insert(0,data)

    def isEmpty(self):
        return len(self.items) == 0

    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)    