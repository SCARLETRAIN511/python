#python3

class ListNode:
    def __init__(self):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self,head):
        prev = None
        curr = head
        while curr != None:
            #store the next node
            nextTemp = curr.next

            #star reversing
            curr.next = prev
            #move the node to the next
            prev = curr
            curr = nextTemp
        
        return prev
    
    
    #use recursion
    def reverseList(self,head):
        if (head == None) or head.next == None:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p