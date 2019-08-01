import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,3*np.pi,0.1)
ysin=np.sin(x)
plt.subplot(1,2,1)
plt.plot(x,ysin)
plt.show()