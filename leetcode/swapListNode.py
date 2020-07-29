#python3

#swap the adjacent node in the linkedlist
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self,head):
        #use recursion to do the swap
        if head == None or head.next == None:
            return head
        next = head.next
        head.next = self.swapPairs(next.next)
        next.next = head
        return next


if __name__ == "__main__":
    s = Solution()
    l1 = ListNode(1)
    l1.next = ListNode(2)

    print(s.swapPairs(l1))

