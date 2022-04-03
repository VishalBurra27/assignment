import numpy as np
import matplotlib.pyplot as plt

def f(x,a,b):
    return x**3+a*x+b

xlist = np.linspace(-4,1,num=1000)

a=-19
b=-30
ylist = f(xlist,a,b)

plt.figure(num=0,dpi=120)
plt.plot(xlist,ylist,label="$y=x^3-19x-30$")
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(color = 'black')
plt.axvline(color = 'black')
plt.legend()
plt.show()
