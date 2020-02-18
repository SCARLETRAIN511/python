# python3
#this is the efficient way to do the fibonacci list
def fibList(n):
    flist=[0 for _ in range(n+1)]
    flist[0]=0
    flist[1]=1
    for i in range(2,n+1):
        flist[i] = flist[i-1]+flist[i-2]
    return flist[n]
    
if __name__ == "__main__":
    print(fibList(6))