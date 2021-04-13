#python3
class ListNode:
    def __init__(self):
        self.val = x
        self.next = None

class Solution:
    def deleteCycle(self,head):
        visited = set()
        while head != None:
            if head in visited:
                return head
            visited.add(head)
            head = head.next
        
        return None

def fun1():
    a = int(input())
    b = int(input())
    c = a + b
    print(c)

import sys

if __name__ == "__main__":
    # 读取第一行的n
    str1 = list(sys.stdin.readline().strip())
    print(str1)
    newStr = []
    for i in str1:
        if i in newStr:
            continue
        else:
            newStr.append(i)
    final = ""
    for j in newStr:
        final += j
    print(final)

