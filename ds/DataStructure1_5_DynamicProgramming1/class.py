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
#compute from small 
def DPchange(money,coins):
    #initiate the table
    MinNumCoins = [0 for i in range(0,money+1)]
    for m in range(1,money+1):
        MinNumCoins[m] = 100000
        for coin in coins:
            if m >= coin:
                #coin == money, one coin is needed
                NumCoins = MinNumCoins[m-coin] + 1
                if NumCoins < MinNumCoins[m]:
                    MinNumCoins[m] = NumCoins
    if MinNumCoins[money] == 100000:
        print('This can not be achieved')
        return False
    else:              
        return MinNumCoins[money]

def EditDistance(A,B):-->A is alist 
    pass
    




if __name__ == "__main__":
    print(RecursiveNumCoins(2,[6,5,1]))
    print(DPchange(997,[2,4,8]))