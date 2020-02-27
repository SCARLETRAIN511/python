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



if __name__ == "__main__":
    print(MultPoly([1,2],[3,4],2))
        

