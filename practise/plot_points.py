import numpy as np
import matplotlib.pyplot as plt

# convert points from euclidian to homogeneous
def to_homog(points):
        points=np.vstack([points,[1,1,1,1]])
        points_homog=points
        return points_homog

# convert points from homogeneous to euclidian
def from_homog(points_homog):
    points=np.delete(points_homog,3,axis=0)
    return points

# project 3D euclidian points to 2D euclidian
def project_points(P_int, P_ext, pts):
    mat_t=np.dot(P_int,P_ext)
    pts_2d=np.dot(mat_t,to_homog(pts))
    print(pts_2d)
    return pts_2d

def camera1():
        P_int_proj = np.eye(3, 4)
        P_ext = np.eye(4, 4)
        return P_int_proj, P_ext

def camera2():
        P_int_proj = np.eye(3, 4)
        print(P_int_proj)
        P_ext=np.array([[1,0,0,0],[0,1,0,0],[0,0,1,1],[0,0,0,1]])
        return P_int_proj, P_ext

def camera3():
        P_int_proj=np.array([[1,0,0,0],[0,1,0,0],[0,0,1,0]])
        rot_y=np.array([[np.cos(60*np.pi/180),0,np.sin(60*np.pi/180),0],[0,1,0,0],[-np.sin(60*np.pi/180),0,np.cos(60*np.pi/180),0],[0,0,0,1]])
        rot_z=np.array([[np.cos(30*np.pi/180),-np.sin(30*np.pi/180),0,0],[np.sin(30*np.pi/180),np.cos(30*np.pi/180),0,0],[0,0,1,0],[0,0,0,1]])
        t1=np.array([[1,0,0,0],[0,1,0,0],[0,0,1,1],[0,0,0,1]])
        P_ext=np.dot(rot_y,rot_z)
        P_ext=np.dot(t1,P_ext)
        return P_int_proj, P_ext

def camera4():
        P_int_proj=np.array([[5,0,0,0],[0,5,0,0],[0,0,5,0]])
        rot_y=np.array([[np.cos(60*np.pi/180),0,np.sin(60*np.pi/180),0],[0,1,0,0],[-np.sin(60*np.pi/180),0,np.cos(60*np.pi/180),0],[0,0,0,1]])
        rot_z=np.array([[np.cos(30*np.pi/180),-np.sin(30*np.pi/180),0,0],[np.sin(30*np.pi/180),np.cos(30*np.pi/180),0,0],[0,0,1,0],[0,0,0,1]])
        t1=np.array([[1,0,0,0],[0,1,0,0],[0,0,1,13],[0,0,0,1]])
        P_ext=np.dot(rot_y,rot_z)
        P_ext=np.dot(t1,P_ext)
        return P_int_proj, P_ext


# test code. Do not modify

def plot_points (points, title='', style='.-r', axis=[]):
    inds = list(range(points.shape[1])) + [0]
    plt.plot(points[0, inds], points[1, inds], style)
    if title:
        plt.title(title)
    if axis:
        plt.axis('scaled')
        # plt.axis(axis)

def main():
    point1 = np.array([[-1, -0.5, 2]]).T
    point2 = np.array([[1, -0.5, 2]]).T
    point3 = np.array([[1, 0.5, 2]]).T
    point4 = np.array([[-1, 0.5, 2]]).T
    points = np.hstack((point1, point2, point3, point4))
    
    for i, camera in enumerate([camera1, camera2, camera3, camera4]):
        P_int_proj, P_ext = camera()
        plot_points(project_points(P_int_proj, P_ext, points), title='Camera %d Projective' %(i + 1), axis=[-0.6, 0.6, -0.6, 0.6])
        plt.show()
        
main()
