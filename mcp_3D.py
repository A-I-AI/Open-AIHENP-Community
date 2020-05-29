import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax  = fig.add_subplot(111, projection='3d')

xn =[1,0,0,0,0]
yn =[0,0,0,0,0]
zn =[0,1,0,0,0]

xc =[0,1,1,1,1]
yc =[0,0,1,1,1]
zc =[0,1,1,1,1]
                                             
ax.scatter(xn, yn, zn, c='navy', marker='o', label='NC')
ax.scatter(xc, yc, zc, c='orangered', marker='*', label='Cosmic' )

ax.set_xlabel('CVN Cosmic ID')
ax.set_ylabel('Leading Shower Energy')
ax.set_zlabel('Number of Prongs')

plt.legend(loc='upper left', numpoints=1, ncol=3, fontsize=8, bbox_to_anchor=(0, 0))
plt.show()






