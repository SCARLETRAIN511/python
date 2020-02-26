# python3
import sys


def compute_min_refills(distance, m, stops):
    # write your code here
    #m is number of stations
    numRefills = 0
    currenRefill = 0#where we are currently standing
    stops.insert(0, 0)
    stops.append(distance)
    while currenRefill <= len(stops)-2:
        lastRefill = currenRefill
        while currenRefill <=len(stops)-2 and stops[currenRefill+1]-stops[lastRefill]<=m:
        #make sure it does not exceed the gas stations and it is small or equal to the distance with the fuel can travel
            currenRefill+=1
        if currenRefill == lastRefill:#even can not go to the next stations
            return -1
        if currenRefill <= len(stops)-2:
            numRefills+=1#if success, increase the number here
        
    return numRefills

if __name__ == "__main__":
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))



