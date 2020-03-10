#python3

class Array(object):
    def __init__(self,size = 32):
        self._size = size
        self._items = [None] * 32
    
    def __getItem__(self,index):
        return self._items[index]

    def __setItem__(self,index,value):
        self._items[index] = value

    def __len__(self,):
        return self._size

    def clear(self, value = None):
        for i in range(len(self._items)):
            self._items[i] = value
    
    def __iter__(self):
        for item in self._items:
            yield item


if __name__ == "__main__":
    testArray = Array(10)
    testArray.__setItem__(5,10)
    print(testArray._items)