#python3

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self,head):
        #return the listNode
        A = [head]
        while A[-1].next:
            A.append(A[-1].next)
        
        return A[len(A)//2]