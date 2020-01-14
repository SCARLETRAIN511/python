#use recursion to return the minimum number of currency for the change.
#Recursion practise 2
#Jiaxuan Tang
#
#

def recMc(coinValueList, change):
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMc(coinValueList, change - i)
            if numCoins < minCoins:
                minCoins = numCoins
    return minCoins


def recDc(coinValueList, change, knownResults):
    minCoins = change
    if change in coinValueList:
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recDc(coinValueList, change - i, knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins
    return minCoins


def dpMakeChange(coinValueList, change, minCoins):
    for cents in range(1, change + 1):
        cointCount = cents
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents - j] + 1 < cointCount:
                cointCount = minCoins[cents - j] + 1
        minCoins[cents] = cointCount
    return minCoins[change]


if __name__ == "__main__":
    print(recDc([1,5,10,50,100], 200, [0]*300))
    print(dpMakeChange([1,3,5,10,50],130,[0]*150))

