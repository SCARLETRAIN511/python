largest = -1
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : 
        break
    try:
        numf=float(num)
        #to calculate maximum
        if numf>largest:
            largest=numf
        if smallest is None:
            smallest=numf
        elif numf<smallest :
            smallest=numf
    except:
        print('Invalid input')
        continue
print('Maximum is',largest)
print('Minimum is',smallest)
