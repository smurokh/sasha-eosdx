import numpy as np
from numpy import genfromtxt
from numpy import savetxt
#from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def fix_dead_pixels(xrd):
    xrd_fixed = np.copy(xrd)
    rows, cols = xrd_fixed.shape
    for i in range(rows):
        for j in range(cols):
            if xrd_fixed[i, j] == 0:
                neighbors = []
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if 0 <= i + dx < rows and 0 <= j + dy < cols and (dx != 0 or dy != 0):
                            neighbor_value = xrd_fixed[i + dx, j + dy]
                            if neighbor_value != 0:
                                neighbors.append(neighbor_value)
                if neighbors:
                    xrd_fixed[i, j] = np.mean(neighbors)
                else:
                    xrd_fixed[i, j] = np.nan
    return xrd_fixed

a = genfromtxt('BA_.csv', delimiter=',')
c = genfromtxt('peakBA_.csv', delimiter=',')
a = fix_dead_pixels(a)
b = np.fft.fft2(a)
d = np.fft.fft2(c)
d = np.subtract(b,d)
d = np.fft.ifft2(d)
d = np.log(d)
#a = np.log(a)
plt.figure(figsize=(8, 8))
#plt.imshow(a, cmap='hot')
plt.imshow(np.abs(d), cmap='hot')
plt.show()

