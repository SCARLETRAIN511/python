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
    print(solution(4,8))
    print(solutionEfficient(357,234))
