import matplotlib.pyplot as plt
import numpy as np

def plot1():
    x=np.linspace(-3,3,50)
    print(x)
    y1=x*2
    y2=x**2
    plt.figure(num=6, figsize=(8,5),)
    plt.plot(x,y1)
    plt.plot(x,y2,color="red",linewidth=1.0,linestyle='--')
    plt.show()

if __name__ == "__main__":
    plot1()