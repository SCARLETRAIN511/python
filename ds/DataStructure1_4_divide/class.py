#divide and conquer

##linear search
def linearSearch(array1,element):
    found = False
    for i in array1:
        if i == element:
            found = i
            break
    return found

#recursive way
def linearSearchRecursion(A,low,high,key):
    #low = lower bound
    #high = higher bound
    if high<low:
        return "Not Found"
    if A[low] == key:
        return low
    return linearSearchRecursion(A,low+1,high,key)


#binary search
##searching sorted data

def binarySearch(A,low,high,key):
    A.sort()
    if high<low:
        return low - 1
    mid = int(low + (high-low)/2)
    if key == A[mid]:
        return mid
    elif key < A[mid]:
        return binarySearch(A,low,mid-1,key)
    else:
        return binarySearch(A,mid+1,high,key)

##polynomial multiplication
#naive algorithm

def MultPoly(A,B,n):
    product = [0 for i in range(2*n-1)]
    for i in range(n):
        for j in range(n):
            product[i+j]=product[i+j]+A[i]*B[j]
    return product

#divide and conquer algorithm
def MultPolyDC(A,B,n,a1,b1):
    R=[i for i in range(2*n-1)]
    if n==1:
        R[0]=A[a1]*B[b1]
        return R
    for i in range(n-1):
        MultPolyDC(A,B,n/2,a1,b1)
    for i in range(n,2*n-1):
        MultPolyDC(A,B,n/2,a1+n/2,b1+n/2)
    DoE1=MultPolyDC(A,B,n/2,a1,b1+n/2)
    D1Eo=MultPolyDC(A,B,n/2,a1+n/2,b1)
    for i in range(n/2,n+n/2-1):
        R[i] += D1Eo+DoE1
    return R


##Master theorem
#T(n)=aT([n/b])+O(n^d)
#O(n^d) O(n^d log(n))


if __name__ == "__main__":
    print(MultPoly([1,2],[3,4],2))
        

