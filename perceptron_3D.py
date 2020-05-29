import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax  = fig.add_subplot(111, projection='3d')

xn =[0.5,  0.32, 0.21, 0.01, 0.001]
yn =[0.27, 0.33, 0.65, 0.91, 1.10]
zn =[4,    3,    5,    5,    4]

xc =[0.45, 0.67, 0.91, 0.87, 0.72]
yc =[0.11, 0.09, 0.05, 0.01, 0.03]
zc =[4,    2,    1,    1,    2]

ax.scatter(xn, yn, zn, c='navy', marker='o', label='NC')
ax.scatter(xc, yc, zc, c='orangered', marker='*', label='Cosmic' )

ax.set_xlabel('CVN Cosmic ID')
ax.set_ylabel('Leading Shower Energy')
ax.set_zlabel('Number of Prongs')

plt.legend(loc='upper left', numpoints=1, ncol=3, fontsize=8, bbox_to_anchor=(0, 0))
plt.show()






