# python3
import numpy

# Discrete Knapsack problem without repetition
def maxGold(W, n, items):
    """ Outputs the maximum weight of gold that fits in knapsack of capacity W
    (int, int, list) -> (int, 2D-array) """

    value = numpy.zeros((W+1, n+1))
    for i in range(1, W+1):
        for j in range(1, n+1):
            # if item i is not part of optimal knapsack
            value[i][j] = value[i][j-1]
            if items[j-1]<=i:
                # if item i is part of optimal knapsack
                temp = value[i-items[j-1]][j-1] + items[j-1]
                # max(i in knapsack, i not in knapsack)
                if temp > value[i][j]:
                    value[i][j] = temp

    return (int(value[W][n]), value)

        
if __name__ == '__main__':
    W, n               = [int(i) for i in input().split()]
    item_weights       = [int(i) for i in input().split()]
    max_weight, Matrix = maxGold(W, n, item_weights)
    print(max_weight)
