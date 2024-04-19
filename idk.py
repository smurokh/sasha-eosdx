import numpy as np
from numpy import genfromtxt
from numpy import savetxt
#from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

for item in ["112_SC1", "112_SC2", "112_SC3", "112_SC4", "112_SC5", "136_SC1", "136_SC2", "136_SC3", "136_SC4", "136_SC5"]:
    a = genfromtxt((f'data/c/SLA1_{item}.csv'), delimiter=',')
    b = genfromtxt((f'data/c/peak_{item}.csv'), delimiter=',')
    a = np.fft.fft2(a)
    b = np.fft.fft2(b)
    c = np.absolute(np.subtract(a,b))
    c = np.divide(c, c[0][0])
    #savetxt(f'data/c_norm/norm_{item}.txt', c, delimiter=', ')

for item in ["112_ST1", "112_ST2", "112_ST3", "112_ST4", "112_ST5", "136_ST1", "136_ST2", "136_ST3", "136_ST4", "136_ST5"]:
    a = genfromtxt((f'data/t/SLA1_{item}.csv'), delimiter=',')
    b = genfromtxt((f'data/t/peak_{item}.csv'), delimiter=',')
    a = np.fft.fft2(a)
    b = np.fft.fft2(b)
    c = np.absolute(np.subtract(a,b))
    c = np.divide(c, c[0][0])
    #savetxt(f'data/t_norm/norm_{item}.txt', c, delimiter=', ')

d= np.zeros([256, 256])

for item in ["112_SC1", "112_SC2", "112_SC3", "112_SC4", "112_SC5", "136_SC1", "136_SC2", "136_SC3", "136_SC4", "136_SC5"]:
    f = genfromtxt((f'data/c_norm/norm_{item}.txt'), delimiter=', ')
    d = np.add(d, f)

for item in ["112_ST1", "112_ST2", "112_ST3", "112_ST4", "112_ST5", "136_ST1", "136_ST2", "136_ST3", "136_ST4", "136_ST5"]:
    f = genfromtxt((f'data/t_norm/norm_{item}.txt'), delimiter=', ')
    d = np.add(d, f)
d = np.divide(d,20)

x = np.empty([20, 65536])
count = 0
for item in ["112_SC1", "112_SC2", "112_SC3", "112_SC4", "112_SC5", "136_SC1", "136_SC2", "136_SC3", "136_SC4", "136_SC5"]:
    a = genfromtxt((f'data/c_norm/norm_{item}.txt'), delimiter=', ')
    a = np.divide(a,d)
    a = np.ravel(a)
    x[count]=a
    count+=1


for item in ["112_ST1", "112_ST2", "112_ST3", "112_ST4", "112_ST5", "136_ST1", "136_ST2", "136_ST3", "136_ST4", "136_ST5"]:
    a = genfromtxt((f'data/t_norm/norm_{item}.txt'), delimiter=', ')
    a = np.divide(a,d)
    a = np.ravel(a)
    x[count]=a
    count+=1

#print(x)
'''
pca = PCA(n_components=3)
fitted = pca.fit(x)
transformed = pca.transform(x)
#print(transformed)
x = transformed[:, 0]
y = transformed[:, 1]
z = transformed[:, 2]

# Create 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the first 14 points in one color
ax.scatter(transformed[:10, 0], transformed[:10, 1], transformed[:10, 2], color='blue')

# Plot the other 14 points in another color
ax.scatter(transformed[10:, 0], transformed[10:, 1], transformed[10:, 2], color='red')

# Set labels and title
ax.set_xlabel('pc0')
ax.set_ylabel('pc1')
ax.set_zlabel('pc2')


#plt.show()

'''

a = genfromtxt('data/og/SLA1_112_SC1.txt', delimiter=' ')
a = np.fft.fft2(a)
b = genfromtxt('data/c/peak_112_SC1.csv', delimiter=',')
b = np.fft.fft2(b)
c = np.subtract(b,a)
#b = np.log(a + 1)
plt.figure(figsize=(8, 8))
plt.imshow(np.abs(c), cmap='hot', extent=(-128, 128, -128, 128))
plt.title('X-Ray Diffraction Pattern')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()