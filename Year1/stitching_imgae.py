import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
path1='C:\\Users\\tangj\\Desktop\\p5.jpg'
path2='C:\\Users\\tangj\\Desktop\\p6.jpg'
im1=cv2.imread(path1)
im2=cv2.imread(path2)

im1=cv2.cvtColor(im1,cv2.COLOR_BGR2RGB)
im2=cv2.cvtColor(im2,cv2.COLOR_BGR2RGB)

im1_small=cv2.resize(im1,(0,0),fx=0.4,fy=0.4,interpolation=cv2.INTER_AREA)
im2_small=cv2.resize(im2,(0,0),fx=0.4,fy=0.4,interpolation=cv2.INTER_AREA)

max_feature=200
orb=cv2.ORB_create(max_feature)
keypoint1,descriptor1=orb.detectAndCompute(im1_small,None)
keypoint2,descriptor2=orb.detectAndCompute(im2_small,None)

im_vis1=cv2.drawKeypoints(im1_small,keypoint1,np.array([]),(100,255,100),cv2.DRAW_MATCHES_FLAGS_DEFAULT)
im_vis2=cv2.drawKeypoints(im2_small,keypoint2,np.array([]),(100,255,100),cv2.DRAW_MATCHES_FLAGS_DEFAULT)

plt.subplot(1,2,1)
plt.imshow(im_vis1)
plt.subplot(1,2,2)
plt.imshow(im_vis2)
plt.show()

matcher=cv2.DescriptorMatcher_create(cv2.DescriptorMatcher_BRUTEFORCE_L1)
matches=matcher.match(descriptor1,descriptor2,None)
matches.sort(key=lambda x:x.distance,reverse=False)

print(matches[0].queryIdx,matches[0].trainIdx,matches[0].distance)

Good_match_percent=0.2
numGoodMatch=int(len(matches)*Good_match_percent)
good_matches=matches[:numGoodMatch]
print(len(good_matches))

imMatch=cv2.drawMatches(im1_small,keypoint1,
                        im2_small,keypoint2,
                        good_matches,None)
plt.imshow(imMatch)
plt.show()

points1=np.zeros((len(good_matches),2),dtype=np.float32)
points2=np.zeros((len(good_matches),2),dtype=np.float32)

for ind,match in enumerate(good_matches):
    points1[ind,:]=keypoint1[match.queryIdx].pt
    points2[ind,:]=keypoint2[match.trainIdx].pt

H,mask=cv2.findHomography(points2,points1,
                        cv2.RANSAC,maxIters=30)

height,width=im2_small.shape[:2]
outstitch=np.zeros((height,width*4,3),np.uint8)a
img1warp=cv2.warpPerspective(im2_small,H,(width*2,height))
img1warp[:,:width]=im1_small
img1warp=img1warp[:,:600]
plt.imshow(img1warp)
plt.show()