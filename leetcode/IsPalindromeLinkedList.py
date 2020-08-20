#python3

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self,head) -> bool:
        vals = []
        currentNode = head
        while currentNode is not None:
            vals.append(currentNode.val)
            currentNode = currentNode.next
        
        return vals == vals[::-1]
    

class Solution2:
    def isPalindrome(self,head) -> bool:
        if head is None:
            return True
        firstHalfEnd = self.endOfFirstHalf(head)
        secondHalfStart = self.reverseList(firstHalfEnd.next)

        result = True
        firstPosition = True
        secondPosition = secondHalfStart

        while result and secondPosition is not None:
            if firstPosition.val != secondPosition.val:
                result = False
            firstPosition = firstPosition.next
            secondPosition = secondPosition.next

        firstHalfEnd.next = self.reverseList(secondHalfStart)
        return result        
    
    def endOfFirstHalf(self,head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def reverseList(self,head):
        previous = None
        current = head
        while current is not None:
            nextNode = current.next
            current.next = previous
            previous = current
            current = nexNode
        return previous