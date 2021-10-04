#Euclidian Vector Representation
import numpy as np
from matplotlib import pyplot as plt
import math
plt.rcParams["figure.figsize"]=[7.00,3.50]
plt.rcParams["figure.autolayout"]=True
data = np.array([[1, 1],[1,0],[0,1]]) #(x-coordinate,y-coordinate)
origin = np.array([[0, 0, 0], [0, 0, 0]])
plt.quiver(*origin, data[:, 0], data[:, 1], color=['black'], scale=15)
plt.show()
# plt.savefig("/home/shivanand/Documents/Euclidian.png",bbox_inches='tight')
plt.savefig("euclidian_vector.png", bbox_inches='tight')
plt.close()
#Hyperbolic Vector Representation
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 100)

r = np.sqrt(100)

x1 = r*np.cos(theta)
x2 = r*np.sin(theta)

# fig, ax = plt.subplots(1)

# plt.plot(x1, x2)
# ax.set_aspect(1)

# plt.xlim(-1.25,1.25)
# plt.ylim(-1.25,1.25)

# plt.grid(linestyle='--')

# plt.savefig("plot_circle_matplotlib_01.png", bbox_inches='tight')

# plt.show()
# plt.
u1=0
v1=1
u2=9.5
v2=2.6
c=pow((u2-u1),2)+pow((v2-v1),2)
# print(c)
l=2*v1*v2
ans=math.acosh(1+2*(c/l))
print(ans)
x = np.arange(0,9.5,0.1) 
y= (np.arccosh(x))
# print(y)
fig, ax = plt.subplots(1)
ax.set_aspect(1)

plt.plot(x,-y)
ax.arrow(1, 0, 8, -2.5, head_width=0.5, head_length=1, fc='k', ec='k')
# plt.plot(x+1,(-y/2)+5)
plt.plot(-x,y)
# plt.plot(-x+3,y+5)
plt.plot(x,y)
ax.arrow(1, 0, 8, 2.5, head_width=0.5, head_length=1, fc='k', ec='k')
plt.plot(-x,-y)
# plt.arrow(0, 0, *(np.arange(1,2,3,4)), width=0.01, color="r")
# plt.arrow(0, 0, *(np.arange(1,2,3,4)), width=0.01, color="g")
plt.plot(x1, x2)
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.grid(linestyle='--')
plt.show()