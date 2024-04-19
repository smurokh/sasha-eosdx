import numpy as np
from numpy import genfromtxt
from numpy import savetxt
m = genfromtxt('mouse/lettersabs/BAabs.txt', delimiter=', ')
m = np.divide(m, m[0][0])
d = m
for item in ('B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'):
    m = genfromtxt((f'mouse/lettersabs/B{item}abs.txt'), delimiter=', ')
    m = np.divide(m, m[0][0])
    d = np.add(d, m)

for item in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14'):
    m = genfromtxt((f'mouse/numsabs/B0{item}abs.txt'), delimiter=', ')
    m = np.divide(m, m[0][0])
    d = np.add(d, m)

d = np.divide(d,28)

for item in ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'):
    a = genfromtxt((f'mouse/lettersabs/B{item}abs.txt'), delimiter=', ')
    a = np.divide(a,d)
    #savetxt(f'B{item}divided.txt', a, delimiter=', ')

for item in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14'):
    a = genfromtxt((f'mouse/numsabs/B0{item}abs.txt'), delimiter=', ')
    a = np.divide(a,d)
    #savetxt(f'B0{item}divided.txt', a, delimiter=', ')


x = np.empty([28, 65536])
count = 0
for item in ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'):
    a = genfromtxt((f'mouse/lettersabs/B{item}abs.txt'), delimiter=', ')
    a = np.divide(a,d)
    a = np.ravel(a)
    x[count]=a
    count+=1


for item in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14'):
    a = genfromtxt((f'mouse/numsabs/B0{item}abs.txt'), delimiter=', ')
    a = np.divide(a,d)
    a = np.ravel(a)
    x[count]=a
    count+=1

x = np.array(x)
    
x = np.array([row[~np.isnan(row)] for row in x])

from sklearn.decomposition import PCA
pca = PCA(n_components=3)
fitted = pca.fit(x)
transformed = pca.transform(x)

import matplotlib.pyplot as plt

x = transformed[:, 0]
y = transformed[:, 1]
z = transformed[:, 2]

# Create 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the first 14 points in one color
ax.scatter(transformed[:14, 0], transformed[:14, 1], transformed[:14, 2], color='blue')

# Plot the other 14 points in another color
ax.scatter(transformed[14:, 0], transformed[14:, 1], transformed[14:, 2], color='red')

# Set labels and title
ax.set_xlabel('pc0')
ax.set_ylabel('pc1')
ax.set_zlabel('pc2')
#plt.show()
