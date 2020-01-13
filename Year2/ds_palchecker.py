from ds1 import Deque

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
    print(palchecker("123454321"))
    print(palchecker("上海自来水来自海上"))
    print(palchecker("lljshishabi"))