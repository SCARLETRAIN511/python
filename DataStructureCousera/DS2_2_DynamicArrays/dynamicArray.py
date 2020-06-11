#dynamic array
#abstract data types

class DynamicArray():
    def __init__(self):
        self.data = []
        self.capacity = 10
        self.size = len(self.data)

    def get(self,i):
        if i>=self.size or i<0:
            return 0
        else:
            return self.data[i]

    def set(self,i,val):
        self.data[i] = val

    def pushBack(self,val):
        self.data.append(val)

    def remove(self,i):
        del self.data[i]


