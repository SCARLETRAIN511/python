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


#removeNth Node from end
#delete the last n node in the linkedlis
class Solution2:
    def removeNthNode(self,head,n):
        length = 0
        #储存头部
        #哑节点
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
            nthNode = nthNode.next
        
        nthNode.next = nthNode.next.next
        #return the head of the linkedlist
        return dummy.next