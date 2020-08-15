#python3

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


#this algorithm checks whether there is a cycle in a linkedList
class Solution:
    def hasCycle(self,head) -> bool:
        nodeSeen = dict()
        while head != None:
            if head in nodeSeen.keys():
                return True
            else:
                nodeSeen[head] = 1
            head = head.next
        return False
        
    def hasCycle2(self,head) -> bool:
        if head == None or head.next == None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast == None or fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next
        
        return True

        


