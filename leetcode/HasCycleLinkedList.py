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
        
