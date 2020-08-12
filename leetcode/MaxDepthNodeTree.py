#python3

class Node:
    def __init__(self,val = None, children = None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self,root) -> int:
        if root is None:
            return 0
        elif root.children == []:
            return 1
        else:
            height = [self.maxDepth(c) for c in root.children]
            return max(height) + 1

if __name__ == "__main__":
    s = Solution()
    t2 = Node(3,[])
    t3 = Node(4,[])
    t1 = Node(1,[t2,t3])
    print(s.maxDepth(t1))