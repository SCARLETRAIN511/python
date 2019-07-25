import numpy as np
from CV_HW4 import compute_H, ransac_H
from numpy import linalg
from random import sample


p1 = np.array([[382, 79], [395, 98], [419, 119], [448, 107], 
    [388, 132], [410, 154], [383, 193], [403, 182], [408, 210], [450, 264],
    [483, 180], [488, 212], [581, 261], [514, 109], [530, 126], [475, 172], 
    [519, 194], [489, 320], [555, 311], [543, 189], [579, 104], [603, 95], 
    [552, 151], [580, 201], [523, 213], [554, 277], [600, 211], [385, 252], 
    [442, 179], [469, 52]])
p2 = np.array([[31, 60], [40, 80],[71, 110], [99, 106], [38, 121], 
    [56, 147], [21, 187], [47, 177], [41, 208], [86, 260], [127, 183], 
    [129, 213], [216, 263], [166, 119], [180, 134], [128, 176], [166, 199], 
    [127, 324], [188, 310], [190, 195], [221, 126], [240, 121], [198, 162], 
    [218, 209], [166, 219], [189, 279], [233, 216], [20, 256], [92, 175], 
    [125, 52]])
matches = np.array([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10],
    [11, 11], [12, 12], [13, 13], [14, 14], [15, 0], [16, 16], [17, 17], [18, 18], [19, 19], [20, 20],
    [21, 21], [22, 22], [23, 23], [24, 24], [25, 25], [26, 26], [27, 27], [28, 28], [29, 29], [0, 15]])


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

h2to1=computeH(p1,p2)

def ransac_H(matches, locs1, locs2, n_iter, tol):
    N = len(matches) # length of locs1, locs2, and matches
    iter = 0
    fit_threshold = 3 # must be between 0 and N. Feel free to adjust.
    bestFit = None
    bestErr = 999999999999999999
    for iter in range(n_iter):
        thisErr = 0
        indexes = sample(range(0, N), 4)
        pairs = matches[indexes]
        maybeInliers = match(locs1, locs2, pairs)
        maybeOutlierMatches = np.delete(matches, indexes, axis=0)
        maybeOutliers = match(locs1, locs2, maybeOutlierMatches)
        maybeModel = computeH(maybeInliers[0], maybeInliers[1])
        alsoInliers = []
        for points in maybeOutliers:
            maybeErr = compute_error(points[0], points[1], maybeModel)  
            if maybeErr < tol:
                thisErr += maybeErr
                alsoInliers.append(points)
            if alsoInliers[0].shape[0] > fit_threshold:
                betterModel = maybeModel
                for maybeInlier in maybeInliers:
                    thisErr += compute_error(maybeInlier[0], maybeInlier[1], betterModel)
                if thisErr < bestErr:
                    bestFit = betterModel
                    bestErr = thisErr
    return bestFit

def match(locs1, locs2, pairs):
    N = len(pairs)
    p1 = p2 = np.zeros((N, 2))
    for i in range(len(pairs)):
        p1[i] = locs1[pairs[i][0]]
        p2[i] = locs2[pairs[i][1]]

    return (p1, p2)



def compute_error(loc1, loc2, H):

    return np.linalg.norm(np.matmul(H, np.append(loc2, 1)) - np.append(loc1, 1)) 
