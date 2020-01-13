def listsum(numlist):
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0] + listsum(numlist[1:])

def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base, base) + convertString[n%base]

if __name__ == "__main__":
    
    print(toStr(12344,2))



    
