#python3

##dynamic programming

def RecursiveNumCoins(money,coins):
    if money == 0:
        return 0
    MinNumCoins = 129999965
    for i in coins:
        if money >= i:
            NumCoins = RecursiveNumCoins(money-i,coins)
            if NumCoins + 1 < MinNumCoins:
                MinNumCoins = NumCoins + 1
    return MinNumCoins

## dynamic programming method 

def DPchange(money,coins):
    MinNumCoins = [0 for i in range(0,money+1)]
    for m in range(1,money+1):
        MinNumCoins[m] = 100000
        for coin in coins:
            if m >= coin:
                NumCoins = MinNumCoins[m-coin] + 1
                if NumCoins < MinNumCoins[m]:
                    MinNumCoins[m] = NumCoins
    return MinNumCoins[money]

if __name__ == "__main__":
    print(RecursiveNumCoins(2,[6,5,1]))
    print(DPchange(997,[2,4,8]))