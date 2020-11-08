#python3

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
    

class Solution:
    def reversePrint(self,head):
        #return the list with int
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        
        return stack[::-1]