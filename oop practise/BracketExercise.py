from stack import Stack

def isMatch(b1,b2):
    if b1 == "(" and b2 ==")":
        return True
    elif b1 == "[" and b2 =="]":
        return True
    elif b1 == "{" and b2 == "}":
        return True
    else:
        return False
    
def main(str1):
    s = Stack()
    index = 0
    isBalanced = True

    while index < len(str1) and isBalanced:
        bracket = str1[index]
        if bracket in "([{":
            s.push(bracket)
        else:
            if s.is_empty():
                isBalanced = False
            else:
                match = s.pop()
                if not isMatch(match,bracket):
                    isBalanced = False
        index += 1
    
    if isBalanced and s.is_empty():
        return True
    else:
        return False

if __name__ == "__main__":
    print(main("()([{{{}}}])(])"))