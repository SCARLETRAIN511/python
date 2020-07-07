#Different bisection algorithms implemented in python


#implemention of the algorithm which find the fixed number in the list

def findFixedPoint(a):
    low = 0
    high = len(a) - 1
    while low < high:
        mid = (low + high) // 2
        if a[mid] < mid:
            low = mid + 1
        elif a[mid] > mid:
            high = mid - 1
        else:
            return a[mid]
    return None


#find the peak in the bitonic peak
def findHighestNum(data):
    low = 0
    high = len(data) - 1

    if len(data) < 3:
        return None
    
    while low <= high:
        mid = (low + high) //2
        midLeft = data[mid-1] if mid - 1 > 0 else float("-inf")
        midRight = data[mid+1] if mid + 1 < len(data) else float("inf")

        if midLeft < data[mid] and midRight > data[mid]:
            low = mid + 1
        elif midLeft > data[mid] and midRight < data[mid]:
            high = mid - 1
        elif midLeft < data[mid] and midRight < data[mid]:
            return data[mid]
    return None


#find the first occurence of the key in the list
def findDuplicatesKey(key,data):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2

        if data[mid] < key:
            low = mid + 1
        elif data[mid] > key:
            high = mid - 1
        else:
            #if the target was finded
            #this is an edge case
            if mid - 1 < 0:
                return mid
            if data[mid - 1] != key:
                return mid
            high = mid - 1


#takes a non-negative integer K and returns the largest integer whose square is less than or equal to the specfied integer K
def intergerSquareRoot(k):
    low = 0
    high = k
    while low <= high:
        mid = (low + high) // 2
        midSquare = mid ** 2
        if midSquare < k:
            low = mid + 1
        elif midSquare > k:
            high = mid - 1
        #if it has the integer solution
        else:
            return mid
    return low - 1



if __name__ == "__main__":
    print(findFixedPoint([1,2,3,4,5,55,343,894]))
    print(findHighestNum([1,2,3,4,5,3,1]))
    print(intergerSquareRoot(227))