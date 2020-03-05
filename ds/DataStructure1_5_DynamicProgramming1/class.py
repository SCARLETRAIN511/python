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


##A and B list with n and m element
def EditDistance(A,B):
    n=len(A)-1
    m=len(B)-1
    small=[i for i in range(len(A))]
    D = [small for i in range(len(B))]
    for j in range(1,len(A)):
        for i in range(1,len(B)):
            insertion = D[i][j-1]+1
            deletion = D[i-1][j]+1
            match = D[i-1][j-1]
            mismatch = D[i-1][j-1]+1
            if A[i] == B[j]:
                D[i][j] = min(insertion,deletion,match)
            else:
                D[i][j] = min(insertion,deletion,mismatch)
    return D[n][m]
##needs revision



if __name__ == "__main__":
    print(RecursiveNumCoins(2,[6,5,1]))
    print(DPchange(997,[2,4,8]))