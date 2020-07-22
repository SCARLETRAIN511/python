class Solution:
    def merge(self,nums1,m,nums2,n) -> None:
        #将nums2 合并到nums1 中
        nums1Copy = nums1[:m]
        nums1[:] = []
        p1 = 0
        p2 = 0

        while p1 < m and p2 < n:
            if nums1Copy[p1] < nums2[p2]:
                nums1.append(nums1Copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1

        if p1 < m:
            nums1[p1 + p2:] = nums1Copy[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]
        
        return nums1


if __name__ == "__main__":
    s = Solution()
    print(s.merge([1,2,3],3,[3,4,5],3))