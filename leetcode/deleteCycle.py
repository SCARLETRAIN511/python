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
