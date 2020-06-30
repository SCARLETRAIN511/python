#algorithms and code about the arrays in python

class SolutionForArrary:
    def arrayAdvanceGame(self,array1):
        furthestReached = 0
        lastidx = len(array1) - 1
        i = 0
        while i <= furthestReached and furthestReached <= lastidx:
            furthestReached = max(furthestReached,array1[i] + i)
            i += 1
        return furthestReached >= lastidx

    def arrayPlusOne(self,data):
        data[-1] += 1
        for i in reversed(range(1,len(data))):
            if data[i] != 10:
                break
            data[i] = 0
            data[i-1] += 1
        if data[i] == 10:
            data[0] = 1
            data.append(0)
        return data


class TwoSum:
    #this is the easiest answer
    def solution1(self,data, targetNumber):
        for i in range(len(data)-1):
            for j in range(i+1,len(data)-1):
                if data[i] + data[j] == targetNumber:
                    print("The answer is " + str(data[i]) + " and " + str(data[j]))
                    return True
        return False

    #use hash table
    def solution2(self, data, targetNumber):
        ht = dict()
        #only o[n] complexity
        for i in range(len(data)):
            if data[i] in ht:
                print(ht[data[i]], data[i])
                return True
            else:
                ht[targetNumber - data[i]] = data[i]
        return False

    def solution3(self,data,targetNumber):
        data.sort()
        print(data)
        i = 0
        j = len(data) - 1
        while i < j:
            if data[i] + data[j] == targetNumber:
                print(data[i],data[j])
                return True
            elif data[i] + data[j] < targetNumber:
                i += 1
            else:
                j -= 1
        print("Not found")
        return False


class OptimnalSolution:
    def solution1(self,data):
        #data is an array with length of 6
        data = sorted(data)
        lengthTime = []
        for i in range(len(data)//2):
            print(data[i],data[~i])
            lengthTime.append(data[i]+data[~i])
        return max(lengthTime)


class IntersectionOfTwoSortedList:
    def solution1(self,array1,array2):
        i = 0
        j = 0
        intersection = []
        #two arrays should be sorted
        while i < len(array1) and j < len(array2):
            if array1[i] == array2[j]:
                if i == 0 or array1[i] != array1[i-1]:
                    intersection.append(array1[i])
                i += 1
                j += 1
            elif array1[i] < array2[j]:
                i += 1
            else:
                 j+= 1
        return intersection


class BuyAndSellStockOnce:
    def solution(self,prices):
        maxProfit  = 0.0
        minPrice = float("inf")
        for price in prices:
            minPrice = min(minPrice,price)
            compareProfit = price - minPrice
            maxProfit = max(maxProfit,compareProfit)
        return maxProfit



if __name__ == "__main__":
    s2 = TwoSum()
    s2.solution3([1,2,3,45,63,4],5)
    s3 = OptimnalSolution()
    s3.solution1([1,2,34,52,32,4])
