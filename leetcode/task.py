def solution(X, Y):
    # write your code in Python 3.6
    #X,Y are arrays
    target=list()
    for i in range(X):
        target.append(X[i]/Y[i])
    
    target.sort()
    begin=0
    end=len(X)-1
    count=0