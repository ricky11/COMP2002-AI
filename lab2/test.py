import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi,np.pi,100)
y = np.sin(x)

plt.figure()
plt.plot(x,y)
plt.title("$y=sin(x)$")
plt.xlabel("$x$")
plt.ylabel("$y$")
plt.savefig("sin2.png")