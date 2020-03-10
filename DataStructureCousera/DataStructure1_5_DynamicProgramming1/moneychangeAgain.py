#python3
import sys

def getChange(m):
    coins = (1,3,4)
    minNumCoins = [m] * (m+1)
    minNumCoins[0]=0

    for i in range(1,m+1):
        for coin in coins:
            if coin <= i:
                numCoins = minNumCoins[i-coin]+1
                if numCoins < minNumCoins[i]:
                    minNumCoins[i]=numCoins
    return minNumCoins[m]

if __name__ == "__main__":
    m = int(sys.stdin.read())
    print(getChange(m))
