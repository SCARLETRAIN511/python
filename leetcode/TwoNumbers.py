# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode,c=0) -> ListNode:
        val=l1.val+l2.val+c
        c=val//10
        #获得进位的值
        
        ret=ListNode(val%10)
        #只用余数 1位
        if (l1.next or l2.next or c!=0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers(l1.next,l2.next,c)
            # use recursion until we can not jump into this loop    
        return ret

if __name__ == "__main__":
    i = 123
    print(i[1])