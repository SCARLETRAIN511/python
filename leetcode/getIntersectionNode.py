#python3


class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self,headA,headB):
        if headA == None or headB == None:
            return None

        pA = headA
        pB = headB
        while pA != pB:
            #any pointer at the end of the linkedlist, it will start at the head of anther linkedlist
            #if there is a common sub linkedlist, they will meet at that point;
            pA = headB if pA is None else p1.next
            pB = headA if pB is None else p2.next
        return pA