#python3
##Dynamic programming Class problems

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




if __name__ == "__main__":
    print(knapsack(10,[6,3,4,2],[30,15,16,9]))