# python 3
import sys

def solution(a,b):
    best = 0
    for i in range(1,min(a,b)+1):
        if a%i==0 & b%i==0:
            if i>best:
                best = i
    return best

#this is the euclidean solution using recursion

def solutionEfficient(a,b):
    if b == 0:
        return a
    else:
        return(solutionEfficient(b,a%b))


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(solutionEfficient(a, b))
