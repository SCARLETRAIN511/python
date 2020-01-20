from ds1 import Deque
from ds1 import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    i = 0
    while i < len(symbolString) and balanced:
        symbol = symbolString[i]
        if symbol in "{[(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        i += 1
    if balanced and s.isEmpty():
        return True
    else:
        return False


#binary number conversion
def binary(decNumber):
    remstack = Stack()
    while decNumber > 0:
        rem = decNumber%2
        remstack.push(rem)
        decNumber = decNumber//2

    binstr = ""
    while not remstack.isEmpty():
        binstr = binstr + str(remstack.pop())
    return binstr


def matches(open, close):
    opens = "{[("
    closers = "}])"
    return opens.index(open) == closers.index(close)


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
    print(binary(1213))