"""
Examen 2D Recuperación
Alexis Saúl Castillo Gonzalez

"""

import matplotlib.pyplot as plt
import numpy as np
import math as mt

#Mis dimensiones y mi titulo

plt.axis("on")

plt.axis([0,100,0,100])

plt.title("TEST 2D")

#Radio del circuclo con mi numero de control
NumCon=1
#Radio
r=NumCon*5

#Mi punto inicial

xc=40
yc=40
Rz=(xc,yc)
alpha1=mt.radians(1)
alpha2=mt.radians(360)
dalpha=mt.radians(1)

#__Punto del circulo

plt.scatter(xc,yc,s=1,color='blue')

print (np.arange(alpha1,alpha2,dalpha))

for alpha in np.arange(alpha1,alpha2,dalpha):

    x=xc+r*mt.sin(alpha)
    y=yc+r*mt.cos(alpha)
    # Color
    plt.scatter(x,y,s=1,color=(0/10, 6/10, 1/10))

#__Punto del circulo

plt.scatter(xc,yc,s=1,color='blue')

print (np.arange(alpha1,alpha2,dalpha))

for alpha in np.arange(alpha1,alpha2,dalpha):

    x=xc+r*mt.sin(alpha)
    y=yc+r*mt.cos(alpha)
    # Color
    plt.scatter(x,y,s=1,color=(0/15, 6/15, 1/15))



#ORIGINAL FIGURE1 IN THE POINT LEFT

x1=xc
x2=5
y1=yc
y2=5

#DRAWE FIGURE

plt.plot([x1,x1],[y1,y2],linewidth=1,color='PURPLE',linestyle="--")
plt.plot([x2,x2],[y1,y2],linewidth=1,color='PURPLE',linestyle="--")
plt.plot([x1,x2],[y1,y1],linewidth=1,color='PURPLE',linestyle="--")
plt.plot([x1,x2],[y2,y2],linewidth=1,color='PURPLE',linestyle="--")

#ORIGINAL FIGURE1 IN THE POINT LEFT

x1=60
x2=20
y1=60
y2=20




plt.show()