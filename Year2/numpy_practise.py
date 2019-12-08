import numpy as np

def main1():
    x=np.array([[1,2,3],
                [2,3,4]])
    print(x.shape[1])
    a=np.zeros((3,4))
    print(a)

def main2():
    a=np.arange(2,20,2).reshape(3, 3)
    print(a)
    a2=np.linspace(1,20,8).reshape(4,2)#divided into 5
    print(a2)
    a3=np.eye(3)# create the I array
    print(a3)

def p1():
    a=np.array([1,2,3,4])
    b=np.arange(4)
    print(a*b)
    print(a>2)#will return an array with booleans

def p2():
    a=np.array([[1,2,3],
                [3,4,5]])
    b=np.linspace(1,13,6).reshape(2,3)
    print(a)
    print(b)
    print(a*b)

def p3():
    a=np.linspace(1,10,4).reshape(2,2)
    b=np.linspace(1,20,4).reshape(2,2)
    print(a)
    print(b)
    print(a.dot(b))
    c=np.linspace(1,5,5)
    d=np.linspace(2,10,5)
    ans=np.dot(c.T,d)
    print('array c is:',c)
    print('array d is:',d)
    print('The answer of c * d is:',ans)

def p4():
    a=np.array([1,2,3,4])
    b=np.array([3,4,5,6])
    c=np.vstack((a,b))
    d=a[:,np.newaxis]
    e=b[:,np.newaxis]
    print(d)
    c2=np.hstack((d,e))
    print(c2)
    print(c)

def p5():
    a=np.arange(12).reshape(3,4)
    print(a)
    print(np.split(a,2,axis=1))#split horizontally
    print(np.split(a,3,axis=0))#split vertically
    print(np.array_split(a,3,axis=1))


if __name__ == "__main__":
    p5()
