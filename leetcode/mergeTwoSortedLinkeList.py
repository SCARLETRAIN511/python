#python3

#merge 2 sorted linkedlist
class ListNode:
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = None


class Solution:
    def mergeTwoLinkedList(self,l1,l2):
        prehead = ListNode(-1)
        prev = prehead
        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        if l1 is not None:
            prev.next = l1
        else:
            prev.next = l2
        return prehead.next


if __name__ == "__main__":
    a = [1,2,3]
    a.pop(3)
    print(a)