
# tb_np_plot.py

import numpy as np
import matplotlib.pyplot as plt

a=3.4
b=0.4
x=np.linspace(0, 30)
y=a*np.exp(x*b)


plt.subplot(311)
plt.plot(x, y)
plt.grid()
plt.xlabel("x")
plt.ylabel("y")

plt.subplot(312)
plt.semilogy(x, y)
plt.grid()
plt.xlabel("x")
plt.ylabel("y")

plt.subplot(313)
plt.loglog(x, y)
plt.grid()
plt.xlabel("x")
plt.ylabel("y")

plt.show()

