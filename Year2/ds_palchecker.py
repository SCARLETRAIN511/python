from ds1 import Deque
from ds1 import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    i = 0
    while i < len(symbolString) and balanced:
        if symbolString[i] == "(":
            s.push(i)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        i += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def palchecker(astring):
    chardeque = Deque()

    for ch in astring:
        chardeque.addRear(ch)
    
    stillEqual = True

    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if first != last:
            stillEqual = False
    return stillEqual

if __name__ == "__main__":
    print(parChecker("(()()())"))
    print(palchecker("上海自来水来自海上"))
    print(palchecker("lljshishabi"))