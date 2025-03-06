import numpy as np
import matplotlib.pyplot as plt
C=1*10**(-6)
R=1590
f=np.logspace(1,6,1000)
#f=np.linspace(10, 10**6,100000)
H=1/(1+1j*2*np.pi*f*R*C)
plt.subplot(211)
plt.semilogx(f,20*np.log10(np.abs(H)))
plt.grid()
plt.xlabel("f(Hz)")
plt.ylabel("dB")
plt.subplot(212)
plt.semilogx(f,np.angle(H,True))
plt.grid()
plt.xlabel("f")
plt.ylabel("deg")
plt.show()