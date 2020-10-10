#python3

class Solution:
    def mergeSort(self,A,m,B,n):
        A[m:] = B
        A.sort()
    
    def mergeSort2(self,A,m,B,n):
        sorted = []
        pa, pb = 0, 0
        while pa < m or pb < n:
            if pa == m:
                sorted.append(B[pb])
                pb += 1
            elif pb == n:
                sorted.append(A[pa])
                pa += 1
            elif A[pa] < B[pb]:
                sorted.append(A[pa])
                pa += 1
            else:
                sorted.append(B[pb])
                pb += 1
        A[:] = sorted



