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

if __name__ == "__main__":
    print(linearSearchRecursion([1,2,3,45,6],0,4,1))