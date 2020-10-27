#python3

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self,head,k):
        #return the listnode
        #use 2 pointers
        former,latter = head,head
        for _ in range(k):
            if not former:
                return
            former = former.next
        
        while former:
            former,latter = former.next,latter.next

        return latter