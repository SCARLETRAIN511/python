#dynamic array
#abstract data types
#python's list is the dynamic array

#bit of coding here
class DynamicArray():
    def __init__(self):
        self.data = []
        self.capacity = 10
        self.size = len(self.data)

    def get(self,i):
        if i>=self.size or i<0:
            return 0
        else:
            return self.data[i]

    def set(self,i,val):
        self.data[i] = val

    def pushBack(self,val):
        self.data.append(val)

    def remove(self,i):
        del self.data[i]


#amotized cost aggregate method = cost(n operations)/n

#amortized method banker's method
#charge extra for each cheap operation. Save the extra charge as tokens in tour ds, use the
#tokens to pay for expensive operations 

#for physict's method
#Define a potential function psi which map states of the data structure to integers
#amotized cost for the operation T= ct+psi(ht) - psi(ht-1)

