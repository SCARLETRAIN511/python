#python3

class Solution:
    def findSubSequence(self,nums):
        n = len(nums)
        if n < 2:
            return []
        b = 201
        hashMap = {}

        def getHash(arr,m):
            key = 0
            for i in range(m):
                key += (arr[i] + 101) * b **(m - 1-i) % 100000007
                key %= 100000007
            return key
        
        def isIncreasing(arr,m):
            for i in range(m-1):
                if arr[i] > arr[i + 1]:
                    return False
            return True
        
        res = []
        for i in range(2**n,2**(n+1)):
            a = bin(i)[3:]
            cur = []
            for j in range(n):
                if a[j] == '1':
                    cur.append(nums[j])
            m = len(cur)
            if m > 1:
                if isIncreasing(cur,m):
                    curkey = getHash(cur,m)
                    if hashMap.get(curkey,-1) == -1:
                        res.append(cur)
                        hashMap[curkey] = 1
                        
        return res