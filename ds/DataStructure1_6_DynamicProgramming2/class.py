#python3
##Dynamic programming Class problems

import numpy as np
#kanpsack problem using dynamic programming
'''
knapsack with repetitions and discrete
greedy algorithms does not apply to discrete knapsack problem
'''
def knapsack(totalWeight,weights,values):
    value = [0] * (totalWeight+1)
    n= len(values)
    #start from if the weight equals to 1
    for w in range(1,totalWeight+1): 
        #try searching in the weights list
        for i in range(1,n):
            #stop when find one smaller than w
            if weights[i] <= w:
                val = value[w-weights[i]] + values[i]
                if val > value[w]:
                    value[w] = val
    return value[totalWeight]


'''
knapsack without repetitions
'''
def KnapSackWithOutRep(Weight, weights, values):
    n = len(values)
    value = np.zeros((Weight+1,n+1),dtype=np.int)
    
    for i in range(1,n+1):
    #gradually increase the number of items that can be taken
        for w in range(1,Weight+1):
            value[w][i] = value[w][i-1]
            if weights[i-1] <= w:
                val = value[w-weights[i-1]][i-2]+values[i-1]
                if value[w][i]<val:
                    value[w][i] = val
    return value[Weight][n]


#Placing parentheses in the equation to maximize the the value
'''
d is the list of digits, op is the list of operations
start from zero
'''

def Parentheses(d,op):
    n = len(d)
    m = np.zeros((d,d),dtype = np.int)
    bigM = np.zeros((d,d),dtype = np.int)
    for i in range(len(n)):
        m[i][i] = d[i]
        bigM[i][i] = d[i]
    for s in range(1,n-1):
        j = 1 + s
        m[i][j] = min(i,j)
        bigM[i][j] = max(i,j)
    return bigM[1][n-1]




if __name__ == "__main__":
    print(knapsack(10,[6,3,4,2],[30,15,16,9]))
    print(KnapSackWithOutRep(10,[6,3,4,2],[30,15,16,9]))