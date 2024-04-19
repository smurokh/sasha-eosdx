import numpy as np
from pprint import pprint

def makearray(s):
    output = []
    s = s.split('\n')
    for item in s:
        item_s=item.split(',')
        output+=[item_s]
    return output


def divide(a):
    c0 = a[0][0]
    c0 = float(c0)
    out = []
    for row in a:
        out1 = []
        for item in row:
            item = item.strip()
            if item!='':
                out1.append(float(item)/c0)
        out+= [out1]
    return out
    
#print(makearray(open('numsabs/B001abs.txt').read().strip()))

a1 = divide(makearray(open('c_abs/112_SC1abs.txt').read().strip()))
a2 = divide(makearray(open('c_abs/112_SC2abs.txt').read().strip()))
a3 = divide(makearray(open('c_abs/112_SC3abs.txt').read().strip()))
a4 = divide(makearray(open('c_abs/112_SC4abs.txt').read().strip()))
a5 = divide(makearray(open('c_abs/112_SC5abs.txt').read().strip()))
a6 = divide(makearray(open('c_abs/136_SC1abs.txt').read().strip()))
a7 = divide(makearray(open('c_abs/136_SC2abs.txt').read().strip()))
a8 = divide(makearray(open('c_abs/136_SC3abs.txt').read().strip()))
a9 = divide(makearray(open('c_abs/136_SC4abs.txt').read().strip()))
a10 = divide(makearray(open('c_abs/136_SC5abs.txt').read().strip()))

aa = divide(makearray(open('t_abs/112_ST1abs.txt').read().strip()))
ab = divide(makearray(open('t_abs/112_ST2abs.txt').read().strip()))
ac = divide(makearray(open('t_abs/112_ST3abs.txt').read().strip()))
ad = divide(makearray(open('t_abs/112_ST4abs.txt').read().strip()))
ae = divide(makearray(open('t_abs/112_ST5abs.txt').read().strip()))
af = divide(makearray(open('t_abs/136_ST1abs.txt').read().strip()))
ag = divide(makearray(open('t_abs/136_ST2abs.txt').read().strip()))
ah = divide(makearray(open('t_abs/136_ST3abs.txt').read().strip()))
ai = divide(makearray(open('t_abs/136_ST4abs.txt').read().strip()))
aj = divide(makearray(open('t_abs/136_ST5abs.txt').read().strip()))

x = np.array([a1,a2,a3,a4,a5,a6,a7,a8,a9,a10])
y = np.array([aa,ab,ac,ad,ae,af,ag,ah,ai,aj])
x1 = x.sum(axis=0)
y1 = y.sum(axis=0)

x1 = np.divide(x1,10)
y1 = np.divide(y1,10)


from numpy import asarray
from numpy import savetxt

a= np.subtract(x1,y1)
b= np.add(x1,y1)
c= np.divide(a,b)

#savetxt('SUBTRACTED_CT.csv', c, delimiter=', ')

c= np.multiply(c,10000)

d= c.astype(int)


#savetxt('subtracted_not_ct.csv', X=d.astype(int), fmt ='%.0f', delimiter=', ')
from numpy import genfromtxt
d = genfromtxt('subtracted_not_ct.csv', delimiter=', ')


    
def makefiles():
    for item in ["112_SC1", "112_SC2", "112_SC3", "112_SC4", "112_SC5", "136_SC1", "136_SC2", "136_SC3", "136_SC4", "136_SC5"]:
        name = item+'norm.csv'
        ar = divide(makearray(open(f'c_abs/{item}abs.txt').read().strip()))
        savetxt(name, ar, delimiter=', ')
    for item in ["112_ST1", "112_ST2", "112_ST3", "112_ST4", "112_ST5", "136_ST1", "136_ST2", "136_ST3", "136_ST4", "136_ST5"]:
        name = item+'norm.csv'
        ar = divide(makearray(open(f't_abs/{item}abs.txt').read().strip()))
        savetxt(name, ar, delimiter=', ')
            
#makefiles()

#row 6 item 6

def make_2c(r,i):
    out = [[],[],[],[],[],[],[],[],[],[]]
    write = ""
    j=0
    for item in ["112_SC1", "112_SC2", "112_SC3", "112_SC4", "112_SC5", "136_SC1", "136_SC2", "136_SC3", "136_SC4", "136_SC5"]:
        name = item+'norm.csv'
        array = open(f'ct_norm/{name}').read().strip()
        array = makearray(array)
        out[j]=array[r][i]
        j+=1
    j=0
    for item in ["112_ST1", "112_ST2", "112_ST3", "112_ST4", "112_ST5", "136_ST1", "136_ST2", "136_ST3", "136_ST4", "136_ST5"]:
        name = item + 'norm.csv'
        array = open(f'ct_norm/{name}').read().strip()
        array = makearray(array)
        out[j]+= ', '
        out[j] += array[r][i]
        j+=1
    for item in out:
        write+=item
        write+="\n"
    with open("R.txt", 'w') as text:
       text.write(write)
        
#make_2c(i,j) 
#make_2c(29,3)

fi = genfromtxt('50.csv', delimiter=',')
fi = np.absolute(fi)
print(np.max(fi))
i,j = np.unravel_index(fi.argmax(), fi.shape)
print(""+str(i)+","+str(j))
print("add 1 to each")
make_2c(int(i),int(j))
fs = genfromtxt('SUBTRACTED_CT.csv', delimiter=',')
print(fs[i,j])