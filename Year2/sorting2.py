#this program includes bubble sorting and its improvements

def bubbleSorting(alist):
    for i in range(len(alist)):
        for j in range(i + 1, len(alist)):
            if alist[i] > alist[j]:
                temp = alist [i]
                alist[i] = alist[j]
                alist[j] = temp
    return alist

#method2
def bubbleSorting1(alist):
    for i in range(len(alist) - 1, 0, -1):
        for j in range(i):
            if alist[j] > alist[j + 1]:
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
    return alist

#improvements on bubble sorting/selection sorting
def bubbleSorting2(alist):
    exchange = True
    passnum = len(alist) - 1
    while passnum > 0 and exchange:
        exchange = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                exchange = True
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
        passnum -= 1
    return alist

#selection sorting
def selectionSorting(alist):
    for fillshot in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillshot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location #get the location of the maximum number in the list
        alist[fillshot], alist[positionOfMax] = alist[positionOfMax], alist[fillshot]
    return alist

#insertion sorting
def insertionSorting(alist):
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index
        while position > 0 and alist[position - 1] > currentvalue:#do the comparsion
            alist[position] = alist[position - 1]#move the value in the list 1 unit next
            position -= 1
        alist[position] = currentvalue
    return alist


#Shell sorting
def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gepInsertionSort(alist, startposition,sublistcount)
        print('After increments of size',sublistcount,'the list is',alist)
        sublistcount = sublistcount//2
    return alist

def gepInsertionSort(alist,start,gap):
    for i in range(start + gap, len(alist), gap):
        currentvalue = alist[i]
        position = i
        while position > 0 and alist[position - 1] > currentvalue:#do the comparsion
            alist[position] = alist[position - 1]#move the value in the list 1 unit next
            position -= gap
        alist[position] = currentvalue
    return alist


#merge sorting
def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i+=1
            else:
                alist[k] = righthalf[j]
                j+=1
            k+=1
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i+=1
            k+=1
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j+=1
            k+=1
    return alist


def mergeSort1(alist):
    if len(alist) <= 1:
        return alist
    #divide the problem
    middle = len(alist)//2
    left = mergeSort1(alist[:middle])
    right = mergeSort1(alist[middle:])

    merged = []

    while left and right:
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    if right:
        merged.extend(right)
    else:
        merged.extend(left)

    return merged

#quick sort
def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)

def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = list.partition(alist,first,last)
        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)
    return alist


if __name__ == "__main__":
    a = [1,42,2,33,331,56,63,2]
    print(quickSort(a))

