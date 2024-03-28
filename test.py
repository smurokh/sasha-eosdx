import numpy as np
from numpy import genfromtxt
from numpy import savetxt

d = genfromtxt('mouse/lettersabs/BAabs.txt', delimiter=', ')
for item in ('B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'):
    d = np.add(d, genfromtxt((f'mouse/lettersabs/B{item}abs.txt'), delimiter=', '))

for item in ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14'):
    d = np.add(d, genfromtxt((f'mouse/numsabs/B0{item}abs.txt'), delimiter=', '))

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


##from sklearn.decomposition import PCA




from numpy import array, dot, mean, std, empty, argsort
from numpy.linalg import eigh, solve
from numpy.random import randn
from matplotlib.pyplot import subplots, show
#data = genfromtxt(('IRISTEST.csv'), delimiter=',')
#data = data[:,:-1]

def cov(X):
    """
    Covariance matrix
    note: specifically for mean-centered data
    note: numpy's `cov` uses N-1 as normalization
    """
    #return dot(X.T, X) / X.shape[0]
    N = data.shape[1]
    C = empty((N, N))
    for j in range(N):
      C[j, j] = mean(data[:, j] * data[:, j])
      for k in range(j + 1, N):
          C[j, k] = C[k, j] = mean(data[:, j] * data[:, k])
    return C

def pca(data, pc_count = None):
    """
    Principal component analysis using eigenvalues
    note: this mean-centers and auto-scales the data (in-place)
    """
    data -= mean(data, 0)
    data /= std(data, 0)
    C = cov(data)
    E, V = eigh(C)
    key = argsort(E)[::-1][:pc_count]
    E, V = E[key], V[:, key]
    U = dot(data, V)  # used to be dot(V.T, data.T).T
    return U, E, V





def plot_pca(data):
    from matplotlib import pyplot as MPL
    clr1 =  '#2026B2'
    fig = MPL.figure()
    ax1 = fig.add_subplot(111)
    data_resc = pca(data, 3)[0]
    ax1.plot(data_resc[:, 0], data_resc[:, 1], '.', mfc=clr1, mec=clr1)
    #MPL.show()
    MPL.savefig('test.png')
data = x
plot_pca(data)
