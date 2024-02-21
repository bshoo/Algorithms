#!/usr/bin/env python3

def inp():
    wl = [0]+list(map(int,input("Enter weights with spaces: ").split()))
    vl = [0]+list(map(int,input("Enter values with spaces: ").split()))
    w = int(input("Enter Total weight: "))
    print(wl)
    print(vl)
    return w, wl, vl

def sack():
    w, wei, val = inp()
    l = len(val)-1
    import numpy as np
    sack = np.full((l+1,w+1),0)
    for i in range(1,l+1):
        for j in range(1,w+1):
            if j-wei[i] >= 0:
                sack[i,j] = max(sack[i-1,j],val[i]+sack[i-1,j-wei[i]])
            if j-wei[i] < 0:
                sack[i,j] = sack[i-1,j]
    print(sack)
    return sack[-1,-1]

def mfsack():
    w, wei, val = inp()
    l = len(val)-1
    import numpy as np
    sack = np.full((l+1,w+1),-1)
    sack[0,:] = 0
    sack[:,0] = 0
    
    maxi = mf(sack, wei, val ,l,w)

    print(sack)
    return maxi

def mf(f, w, v, i, j):
    if f[i,j] < 0 :
        if j<w[i]:
            value = mf(f, w, v, i-1, j)
        else:
            value = max(mf(f, w, v, i-1, j), v[i]+mf(f, w, v, i-1, j-w[i]))
        f[i, j] = value
    return f[i, j]

if __name__ == "__main__":
    #print("Max: ",sack())
    print("Max MF: ",mfsack())

