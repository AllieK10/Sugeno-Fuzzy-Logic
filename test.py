import numpy as np
import matplotlib.pyplot as plt
from SelfFunctions import *

x = np.arange(0, 10, 0.1)
Y = [np.array([mfRYisCur(z) for z in x]),
     np.array([mfRYisRec(z) for z in x]),
     np.array([mfRYisEar(z) for z in x])]

plt.figure(figsize = (10,10))
ax = []
ax.append(plt.subplot(2,2,1))
for y in Y:
    plt.plot(x, y, linewidth = 3)
plt.show()
