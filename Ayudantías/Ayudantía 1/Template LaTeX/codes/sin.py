import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.,10.,1001)
y = np.sin(x)

plt.figure()
plt.plot(x, y, '-')
plt.xlabel('x')
plt.ylabel('y')

# Save figure
path = './figures/'

plt.savefig(path+'sin.pdf')
