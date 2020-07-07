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




if __name__ == "__main__":
    print(findFixedPoint([1,2,3,4,5,55,343,894]))
    print(findHighestNum([1,2,3,4,5,3,1]))