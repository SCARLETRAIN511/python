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


if __name__ == "__main__":
    print(bubbleSorting1([1,2424,2,13,3154,13]))
    print(selectionSorting([15,14,13,12,12,5,6,3,2]))
    print(insertionSorting([5,3,4,1,244,12]))