import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def plot1():
    x=np.linspace(-3,3,50)
    print(x)
    y1=x*2
    y2=x**2
    plt.figure(num=1, figsize=(8,5),)#num1 means the title will be figure1
    plt.plot(x,y1)
    plt.plot(x,y2,color="red",linewidth=1.0,linestyle='--')
    plt.show()

def plot2():
    x = np.linspace(-3,3,50)
    y1 = 2 * x + 1
    y2 = x**2
    plt.figure()
    plt.plot(x,y2)
    plt.plot(x, y1, color='r',linewidth=1.0,linestyle='--')
    plt.yticks([-2,-1,0,2,3],['bad','awful','normal','not bad','good'])
    plt.xlim((-1,2))
    plt.ylim((-2,3))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def plot3():
    x=np.linspace(-3,3,50)
    y1=x*2+1
    y2=x**2
    plt.figure()
    plt.plot(x,y2,label='Square')
    plt.plot(x,y1,color='r',linewidth=1.0,linestyle='--',label='Linear')
    new_ticks=np.linspace(-1,2,5)
    plt.xticks(new_ticks)
    plt.yticks(new_ticks,['really bad','bad','normal','good','very good'])
    ax=plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data','0'))
    plt.legend(loc='bestc')
    plt.show()

def scatter1():
    n=1024
    x=np.random.normal(0,1,n)
    y=np.random.normal(0,1,n)
    t=np.arctan2(y,x)
    plt.scatter(x,y,s=20,c=t,alpha=0.5)
    plt.xlim(-1.5,1.5)
    plt.xticks(())
    plt.ylim(-1.5,1.5)
    plt.yticks(())
    plt.show()

def bar1():
    n=12
    x=np.arange(12)
    y1=(1-x/float(n))*np.random.uniform(0.5,1.0,n)
    y2=(1-x/float(n))*np.random.uniform(0.5,1.0,n)
    plt.bar(x,+y1)
    plt.bar(x,-y2)
    plt.xlim(-0.5,n)
    plt.xticks(())
    plt.yticks(())
    plt.ylim(-1.25,1.25)
    for x,y in zip(x,y1):
        plt.text(x+0.4,y+0.5,'%2f'%y,ha='center',va='bottom')

    for x,y in zip(x,y2):
        plt.text(x+0.4,-y-0.5,'%2f'%y,ha='center',va='top')
    plt.show()

def contour1():
    def f(x,y):
        return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)
    n=256
    x=np.linspace(-3,3,n)
    y=np.linspace(-3,3,n)
    X,Y=np.meshgrid(x,y)
    plt.contour(X,Y,f(X,Y),8,alpha=0.75,cmap=plt.cm.hot)
    c=plt.contour(X,Y,f(X,Y),8,colors='black',linewidth=.5)
    plt.clabel(c,inline=True,fontsize=10)
    plt.xticks(())
    plt.yticks(())
    plt.show()

def Plot3D():
    fig=plt.figure()
    ax=Axes3D(fig)
    x=np.arange(-4,4,0.25)
    y=np.arange(-4,4,0.25)
    X,Y=np.meshgrid(x,y)
    R=np.sqrt(X**2+Y**2)
    Z=np.sin(R)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
    #ax.contourf(X,Y,Z,zdir='x',offset=2,cmap=plt.get_cmap('rainbow'))
    plt.show()

def subPlot():
    plt.figure()
    plt.subplot(221)
    plt.plot([0,1],[0,4])
    plt.subplot(222)
    plt.plot([0,1],[0,4])
    plt.subplot(224)
    plt.plot([0,1],[0,4])
    plt.subplot(223)
    plt.plot([0,1],[0,4])
    plt.show()

if __name__ == "__main__":
    subPlot()