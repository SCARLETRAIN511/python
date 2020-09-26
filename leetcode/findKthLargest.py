#python3

class Solution:
    def findKthLargest(self,nums,k) -> int:
        numsSorted = self.quickSort(nums)
        return numsSorted[-k]

    
    def quickSort(self,alist):
        self.quickSortHelper(alist, 0, len(alist)-1)
        return alist

    def quickSortHelper(self,alist, first, last):
        if first < last:
            splitpoint = self.partition(alist,first,last)
            self.quickSortHelper(alist, first, splitpoint - 1)
            self.quickSortHelper(alist, splitpoint + 1, last)

    def partition(self,alist, first, last):
        pivotValue = alist[first]
        leftmark = first + 1
        rightmark = last
        done = False

        while not done:
            while leftmark <= rightmark and alist[leftmark] <= pivotValue:
                leftmark += 1
            while alist[rightmark] >= pivotValue and rightmark >= leftmark:
                rightmark -= 1
            if rightmark < leftmark:
                done = True
            else:
                temp = alist[leftmark]
                alist[leftmark] = alist[rightmark]
                alist[rightmark] = temp
        temp = alist[first]
        alist[first] = alist[rightmark]
        alist[rightmark] = temp
        return rightmark

if __name__ == "__main__":
    s = Solution()
    print(s.findKthLargest([1,2,3,4,2,3,2,3313],3))