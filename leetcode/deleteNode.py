#python3

#delete the node in the linkedlist
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self,node):
        node.val = node.next.val
        node.next = node.next.next


#delete the last n node in the linkedlis
class Solution2:
    def removeNthNode(self,head,n):
        length = 0
        dummy = ListNode(0)
        dummy.next = head
        first = head
        while first:
            length += 1
            first = first.next
        
        nth = length - n
        nthNode = dummy
        while nth > 0:
            nth -= 1
            dummy = dummy.next
        
        dummy.next = dummy.next.next
        return dummy.next