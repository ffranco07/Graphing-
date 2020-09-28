import numpy as np 
import matplotlib.pyplot as plt 

#x = [1, 2, 3, 4, 5]
#y = [5, 10, 15, 20, 25]
#y2 = [25, 20, 15, 10, 5]

#plt.plot(x, y, "ro")
#plt.plot(x, y2, "b+")
#plt.show()

def math(x):
    return np.sin(x) * x ** 10 * x

x = np.arange(100, -100)
y = math(x)

plt.plot(x, y)
plt.show()