#abstract data structure

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)				

    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def get_stack(self):
        return self.items5

    def __str__(self):
        s = ""
        for i in range(len(self.items)):
            s += str(self.items[i].value + "-")
        return s

    def __len__(self):
        return len(self.items)