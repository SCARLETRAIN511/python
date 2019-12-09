#data structure


class Queue():
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

class Stack():
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)



if __name__ == "__main__":
    a=Queue()
    a.enqueue(1)
    a.enqueue(2)
    a.dequeue()
    print(a.items)
    b=Stack()
    b.push(7)
    b.push('fuck')
    print(b.peek())
    print(b.items)