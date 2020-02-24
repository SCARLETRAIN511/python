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
        pos = NumberList.pos(maxNow)
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

#celebrity problem
#2 children in the group should not differ over 1 year in age, 2 children in one group
#def minGroups(c):
#    m = len(c)
#    for each kinds of combination of groups:
#        good = True #k is number of groups
#        for i in range(1,k):
#            if max(G1)-min(G1)>1:
#                good = False
#        if good:
#            m = min(m,k)
#    return m

##using efficient algorithm
def PointsCoverSorted(x):
    R=[]
    i = 0
    while i<=len(x)-1:
        l,r = x[i],x[i]+1
        R.append([l,r])
        i+=1
        while i<=len(x)-1 and x[i]<=r:
            i+=1
    return R


#lon hike problem
#15kg of food, fit food in the knapsack
#Maximize
#weight w1 w2 w3... values V1 V2 V3...
#choose the value with the biggest V/W

def knapsack(W,weight,value):
    n = len(weight)
    A = [ 0 for i in range(n)]
    V = 0
    v_w = []
    for i in range(n):
        v_w.append(value[i]/weight[i])

    for i in range(n):
        pos = v_w.index(max(v_w))
        if W == 0:
            return (V,A)

        if weight[pos] > 0:

            a = min(weight[pos],W)
            V += a*v_w[pos]
            weight[pos] -= a
            A[pos] += a
            v_w[pos]=0
            #do not need to consider that item anymore
            W -= a           
    return (V,A)


if __name__ == "__main__":
    print(knapsack(15,[3,2,5],[12,6,22]))