# python3

def fibList(n):
    flist=[]
    flist.append(0)
    flist.append(1)
    for i in range(2,n+1):
        flist.append(flist[i-1]+flist[i-2])
    return flist[n]
    
if __name__ == "__main__":
    n=int(input())
    print(fibList(n))