#!/usr/bin/env python
# coding: utf-8

# # Read in RAW Images (Linear)

# In[1]:


# In[2]:


from cv2 import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

path1 = '2631563931832_.pic_hd.jpg'
path2 = '2641563931834_.pic_hd.jpg'
img1 = cv2.imread(path1)
img2 = cv2.imread(path2)

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(15, 8))
plt.imshow(img1)
plt.show()
print(img1.shape)


# In[3]:


img_nn = cv2.resize(img1, (0, 0), fx=1.0/8, fy=1.0/8, interpolation=cv2.INTER_NEAREST)
img_linear = cv2.resize(img1, (0, 0), fx=1.0/8, fy=1.0/8, interpolation=cv2.INTER_LINEAR)
img1_small = cv2.resize(img1, (0, 0), fx=1.0/8, fy=1.0/8, interpolation=cv2.INTER_AREA)
img2_small = cv2.resize(img2, (0, 0), fx=1.0/8, fy=1.0/8, interpolation=cv2.INTER_AREA)

print(img1_small.shape)

plt.figure(figsize=(26, 32))

plt.subplot(2, 2, 1)
plt.imshow(img_nn)
plt.subplot(2, 2, 2)
plt.imshow(img_linear)
plt.subplot(2, 2, 3)
plt.imshow(img1_small)
plt.subplot(2, 2, 4)
plt.imshow(img2_small)
plt.show()

plt.figure(figsize=(15, 8))


# # ORB descriptor

# In[4]:


MAX_FEATURE = 200
orb = cv2.ORB_create(MAX_FEATURE)

keypoint1, descriptor1 = orb.detectAndCompute(img1_small, None)
keypoint2, descriptor2 = orb.detectAndCompute(img2_small, None)
print('descriptor shape:', descriptor1[0], descriptor1.shape)


# # draw keypoints overlay onto image

# In[5]:


img_vis1 = cv2.drawKeypoints(img1_small, keypoint1, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DEFAULT)
img_vis2 = cv2.drawKeypoints(img2_small, keypoint2, np.array([]), (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DEFAULT)
# img_vis1 = cv2.drawKeypoints(img1_small, keypoint1, img1_small, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_OVER_OUTING)
# img_vis2 = cv2.drawKeypoints(img2_small, keypoint2, img2_small, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_OVER_OUTING)

plt.figure(figsize=(20, 10))

plt.subplot(1, 2, 1)
plt.imshow(img_vis1)
plt.subplot(1, 2, 2)
plt.imshow(img_vis2)
plt.show()


# # match feature

# In[6]:


matcher = cv2.DescriptorMatcher_create(cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_L1)
matches = matcher.match(descriptor1, descriptor2, None)
print("First match: %s and total match number %d" %(matches[0], len(matches)))

print(matches[0].queryIdx, matches[0].trainIdx, matches[0].distance) # queryIdx: Feature in first arg; trainIdx: in second arg


# In[7]:


matches.sort(key=lambda x: x.distance, reverse=False)

print(img1_small.shape)
print(matches[0].queryIdx, matches[0].trainIdx, matches[0].distance)

imMatch_unsorted = cv2.drawMatches(img1_small, keypoint1, img2_small, keypoint2, matches, None)

plt.figure(figsize=(26, 32))
plt.imshow(imMatch_unsorted)
plt.show()


# In[8]:


GOOD_MATCH_PERCENT = 0.2
numGoodMatch = int(len(matches) * GOOD_MATCH_PERCENT)
good_matches = matches[:numGoodMatch]
print("Number of good matches: %d" %len(good_matches))

imMatch = cv2.drawMatches(img1_small, keypoint1, img2_small, keypoint2, good_matches, None)

plt.figure(figsize=(26, 32))
plt.imshow(imMatch)
plt.show()


# # extract matching descriptors

# In[9]:


points1 = np.zeros((len(good_matches), 2), dtype=np.float32)
points2 = np.zeros((len(good_matches), 2), dtype=np.float32)

for ind, match in enumerate(good_matches):
    points1[ind, :] = keypoint1[match.queryIdx].pt
    points2[ind, :] = keypoint2[match.trainIdx].pt

print("Coordinates of points", points1)


# # Compute homography

# In[11]:


H21, mask = cv2.findHomography(points2, points1, cv2.RANSAC, maxIters=30)
H12, mask = cv2.findHomography(points1, points2, cv2.RANSAC, maxIters=30)

# print(mask.shape, mask)
print(H12)


# # use computed homography to warp image

# In[12]:


height, width = img2_small.shape[:2]
img1warp = cv2.warpPerspective(img1_small, H12, (width, height))

# overlay1 = 
plt.figure(figsize=(26, 32))
plt.subplot(1, 2, 1)
plt.imshow(img1warp)
plt.subplot(1, 2, 2)
plt.imshow(img1_small)
plt.show()


# In[ ]:




