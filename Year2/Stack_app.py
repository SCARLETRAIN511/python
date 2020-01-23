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

def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"

    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber//2
    
    newStr = ''
    while not remstack.isEmpty():
        newStr = newStr + digits[remstack.pop()]
    
    return newStr


#中缀转后缀算法
def infixToPosfix(infixexpr):
    prec = {}
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIZKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return " ".join(postfixList)


#回文词
def palchecker(astring):
    chardeque = Deque()

    for ch in astring:
        chardeque.addRear(ch)
    
    stillEqual = True

#the length maybe odd or even
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
    print(baseConverter(123,16))
    print(infixToPosfix('( A + B ) * C'))