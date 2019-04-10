fname=input('input the name of the file:')
try:
    f=open(fname)
except:
    print('can not open the file:',fname)
    quit()


