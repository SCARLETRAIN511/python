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


if __name__ == "__main__":
    print(RecursiveNumCoins(2,[6,5,1]))