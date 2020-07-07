#find the closest number in the list to the target number


def findClosestNumber(data,target):
    #set the min difference
    minDiff = float("inf")
    #set 2 pointers
    low = 0
    high = len(data) - 1
    closestNumber = None

    #two extreme conditionshere
    if len(data) == 0:
        return None
    if len(data) == 1:
        return data[0]  
    
    while low <= high:
        mid = (low + high)//2

        if mid < len(data):
            minDiffRight = abs(data[mid] - target)
        if mid > 0:
            minDiffLeft = abs(data[mid-1] - target)


        if minDiffLeft < minDiffRight:
            minDiff = minDiffLeft
            closestNumber = data[mid-1]
        if minDiffRight < minDiffLeft:
            minDiff = minDiffRight
            closestNumber = data[mid]
        
        if data[mid] < target:
            low = mid + 1
        elif data[mid] > target:
            high = mid - 1
        else:
            return data[mid]

    return closestNumber


def main():
    data1 = [1,2,3,4,5,62,532,2334]
    target = 5
    print(findClosestNumber(data1,target))


if __name__ == "__main__":
    main()

