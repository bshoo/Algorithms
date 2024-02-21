#!/usr/bin/env python3

def merge_sort(a,n):
    if n>1:
        b = a[0:int(n/2)]
        c = a[int(n/2):n]
        merge_sort(b,len(b))
        merge_sort(c,len(c))
        mergeback(b,c,a)

def mergeback(b, c, a):
    p = len(b)
    q = len(c)
    i=j=k=0
    while i<p and j<q:
        if b[i] <= c[j]:
            a[k] = b[i]
            i+=1
        else:
            a[k] = c[j]
            j+=1
        k+=1
    #print(a,b,c)
    while i<p:
        a[k] = b[i]
        i+=1; k+=1
    while j<q:
        a[k]=c[j]
        j+=1; k+=1

array = [8,3,2,9,7,1,5,4,6]
print(array)
merge_sort(array,len(array))
print(array)
