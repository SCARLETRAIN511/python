#python3

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self,nums) -> TreeNode:
        def helper(left,right):
            if left > right:
                return None
        
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = helper(left,mid - 1)
            root.right = helper(mid + 1,right)
            return root

        return helper(0,len(nums) - 1)


if __name__ == "__main__":
    s = Solution() 
    sortedList = [1,2,3,4,5,6]
    print(s.sortedArrayToBST(sortedList).val)
        