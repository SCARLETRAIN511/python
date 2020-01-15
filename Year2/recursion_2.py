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


##using dynamic programming to increase the efficiency
def dpMakeChange(coinValueList, change, minCoins):
    #逐个计算最少硬币数
    for cents in range(1, change + 1):
        cointCount = cents#maximum number of coins
        for j in [c for c in coinValueList if c <= cents]:
            #j is the one of the values of the coins
            if minCoins[cents - j] + 1 < cointCount:
                cointCount = minCoins[cents - j] + 1
        minCoins[cents] = cointCount
    return minCoins[change]

 
def dpMakeChange2(coinValueList, change, minCoins, coinsUsed):
    for cents in range(1, change + 1):
        cointCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            #j is the one of the values of the coins
            if minCoins[cents - j] + 1 < cointCount:
                cointCount = minCoins[cents - j] + 1
                newCoin = j
        minCoins[cents] = cointCount
        coinsUsed[cents] = newCoin
    return minCoins[change]

def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin

clist = [1,5,10,21,25]
amout = 63
coinsUsed = [0] * (amout + 1)
coinsCount = [0] * (amout + 1)


if __name__ == "__main__":
    print(dpMakeChange2(clist, amout, coinsCount, coinsUsed))
    printCoins(coinsUsed,amout)