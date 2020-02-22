#lecture problems

def solution(NumberList):
    NumberList.sort(reverse = True)
    MaxNum = ""
    for i in NumberList:
        MaxNum += str(i)
    MaxNum = int(MaxNum)
    return MaxNum

def efficient(NumberList):
    MaxNum = ""
    if len(NumberList) == 0:
        return ""
    else:
        maxNow = max(NumberList)
        MaxNum += str(maxNow)
        pos = NumberList.index(maxNow)
        NumberList.pop(pos)
        return MaxNum + efficient(NumberList)

#carfuel problem
#n gas stations
def MinRefills(x,n,L):
    numRefills = 0
    currentRefill = 0#where we are currently standing

    while currentRefill <= n:
        lastRefill = currentRefill
        while (currentRefill <= n and (x[currentRefill+1]-x[lastRefill])<= L):
        #make sure it does not exceed the gas stations and it is small or equal to the distance with the fuel can travel
            print(x[currentRefill+1]-x[lastRefill])
            currentRefill += 1
            print(currentRefill)
        if currentRefill == lastRefill:#even can not go to the next stations
            return "Impossible"
        if currentRefill <= n:
            numRefills+=1#if success, increase the number here

    return numRefills

if __name__ == "__main__":
    #use this list as an example
    #print(solution([1,2,3,5,1,3,8]))
    #print(efficient([1,2,3,4,5,5,5]))
    x=[0,200,375,550,750,950]
    L = 400
    n = 4
    print(MinRefills(x,n,L))