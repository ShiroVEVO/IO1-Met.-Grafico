import numpy as np
from matplotlib import pyplot as plt

def f1(x):
    return (-3/8)*x+30
def f2(x):
    return (-3)*x+60
def f3(x):
    return (-4/5)*x+40

x=np.arange(-10,80,0.1)

plt.plot(x, [f1(i) for i in x])
plt.plot(x, [f2(i) for i in x])
plt.plot(x, [f3(i) for i in x])

plt.ylim(-10, 50)

plt.axhline(y=0, xmin=0.01, xmax=0.95)
plt.axvline(x=0, ymin=0.01, ymax=0.95)
plt.fill_between(x,f1(x), color="blue", alpha=0.2)
plt.fill_between(x,f2(x), color="blue", alpha=0.2)
plt.fill_between(x,f3(x), color="blue", alpha=0.2)
plt.grid()
plt.show()

