#python3
import random


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



#method editing from qucik search
class Solution2:
    def findKthLargest(self,nums,k):
        return self.quickSelect(0,len(nums)-1,len(nums) - k,nums)

    
    def quickSelect(self,l,r,index,alist):
        q = self.randomPartition(l,r,alist)
        if q == index:
            return alist[q]
        elif q < index:
            return self.quickSelect(q+1,r,index,alist)
        
        return self.quickSelect(l,q-1,index,alist)

    
    def randomPartition(self,l,r,alist):
        i = random.randint(l,r)
        alist[i],alist[r] = alist[r],alist[i]
        return self.partition(alist,l,r)

    def partition(self,alist,l,r):

        x = alist[r]
        i = l-1
        for j in range(l,r):
            if alist[j] <= x:
                i += 1
                alist[i], alist[j] = alist[j], alist[i]
        alist[i+1], alist[r] = alist[r], alist[i+1]

        return i + 1





if __name__ == "__main__":
    s = Solution()
    print(s.findKthLargest([1,2,3,4,2,3,2,3313],3))