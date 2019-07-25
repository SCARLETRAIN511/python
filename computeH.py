from numpy import linalg
import numpy as np
#p1 and p2 are the nx2 array, coordiantes from the two images

def computeH(p1,p2):
    #number of the rows of the points input
    row=p1.shape[0]
    mat_a=np.zeros((2*row,9)) 
    for i in range(row):
        fir=i*2
        sec=i*2+1
        mat_a[fir,:]=[p1[i,0],p1[i,1],1,0,0,0,-p1[i,0]*p2[i,0],-p1[i,1]*p2[i,0],-p2[i,0]]
        mat_a[sec,:]=[0,0,0,p1[i,0],p1[i,1],1,-p1[i,0]*p2[i,1],-p1[i,1]*p2[i,1],-p2[i,1]]
    print(mat_a)
    mat=mat_a.T.dot(mat_a)
    eig_val,eig_vec=linalg.eig(mat)
    index=np.argmin(eig_val)
    min_eigvec=eig_vec[index,:]
    return min_eigvec.reshape((3,3))


