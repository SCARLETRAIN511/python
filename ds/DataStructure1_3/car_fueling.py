# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    #n is the tank here
    numRefills = 0
    currenRefill = 0#where we are currently standing
    while currenRefill <= stops:
        lastRefill = currenRefill
        while currenRefill <=stops & distance[currenRefill+1]-distance[lastRefill]<=tank:
        #make sure it does not exceed the gas stations and it is small or equal to the distance with the fuel can travel
            currenRefill+=1
        if currenRefill == lastRefill:#even can not go to the next stations
            return "Impossible"
        if currenRefill <= stops:
            numRefills+=1#if success, increase the number here
    return numRefills


if __name__ == '__main__':
    print(compute_min_refills([0,200,300,400,500], 200, 4))
