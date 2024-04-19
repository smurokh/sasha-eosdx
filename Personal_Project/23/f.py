import numpy as np

def makearrayt(s):
    output = []
    s = s.split('\n')
    for item in s:
        item_s=item.split(' ')
        output+=[item_s]
    return output

def makearrayc(s):
    output = []
    s = s.split('\n')
    for item in s:
        item_s=item.split(',')
        output+=[item_s]
    return output

def runarray(input):
    return np.fft.fft2(input)

def subtract(a,b):
    return np.subtract(a, b)

def make_files(a):
    output = ""
    for row in a:
        for item in row:
            output+=str(item)
            output+= ", "
        output+="\n"
    return output 

for number in ["112_SC1", "112_SC2", "112_SC3", "112_SC4", "112_SC5", "136_SC1", "136_SC2", "136_SC3", "136_SC4", "136_SC5"]:
    arraya = open(f'Fourier/SLA1_{number}.txt').read().strip()
    arrayb = open(f'c/{number}.csv').read().strip()
    arraya = makearrayt(arraya)
    arrayb = makearrayc(arrayb)
    arraya = runarray(arraya)
    arrayb = runarray(arrayb)
    out = np.absolute(subtract(arraya,arrayb))

    #with open(f'{number}abs.txt', 'w') as text:
    #    text.write(make_files(out))


for number in ["112_ST1", "112_ST2", "112_ST3", "112_ST4", "112_ST5", "136_ST1", "136_ST2", "136_ST3", "136_ST4", "136_ST5"]:
    arraya = open(f'Fourier/SLA1_{number}.txt').read().strip()
    arrayb = open(f't/{number}.csv').read().strip()
    arraya = makearrayt(arraya)
    arrayb = makearrayc(arrayb)
    arraya = runarray(arraya)
    arrayb = runarray(arrayb)
    out = np.absolute(subtract(arraya,arrayb))

    #with open(f'{number}abs.txt', 'w') as text:
    #    text.write(make_files(out))
    