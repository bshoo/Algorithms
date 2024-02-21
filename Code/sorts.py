#!/usr/bin/env python3

import random
import sys
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from os import system
from math import log

sys.setrecursionlimit(10000)

def sel_sort(inp, n):
    for i in range(n-1,0,-1):
        mini = i
        for j in range(i):
            if inp[j] > inp[mini] : mini = j
        if mini != i:
            x = inp[i]
            inp[i] = inp[mini]
            inp[mini]=x

def seq_search(inp, l):
	key = 1
	inp.append(key)
	i = 0
	while inp[i] != key:
		i += 1
	if i==l:
		return
	else:
		return

def bubble_sort(arr, n):
    for i in range(n):
	    for j in range(0, n-i-1):
		    if arr[j] > arr[j+1]:
			    arr[j], arr[j+1] = arr[j+1], arr[j]

def quick_sort(ar, l, r):
    if l < r:
        s = partition(ar, l, r)
        quick_sort(ar, l, s - 1)
        quick_sort(ar, s + 1, r)

def partition(ar, l, r):
    p = ar[int((l+r)/2)] # The choosing of the pivot element changes everything, choosing a random element, or the middle one is generally faster than first or last element
    i = l + 1
    j = r
    while i <= j:
        while i <= j and ar[i] <= p:
            i += 1
        while i <= j and ar[j] >= p:
            j -= 1
        if i < j:
            ar[i], ar[j] = ar[j], ar[i]

    ar[l], ar[j] = ar[j], ar[l]
    return j

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

def ins_sort(a, n):
    for i in range(1, n):
        v = a[i]
        j = i-1
        while j>=0 and a[j] > v:
            a[j+1] = a[j]
            j-=1
        a[j+1] = v

def dcs(a, n):
    u = a[0]
    l = a[0]
    s = [0] * n 
    for i in a:
        if i>u:
            u = i
        if i<l:
            l = i
    d = [0 for _ in range(u-l+1)]
    for i in range(0,n):
        d[a[i]-l] = d[a[i]-l] + 1
    for j in range(1, u-l+1):
        d[j] = d[j-1] + d[j]
    for i in range(n-1, -1, -1):
        j = a[i]-l
        s[d[j]-1] = a[i]
        d[j] = d[j]-1
    return s

def analyze(input_sizes):
    with open("sorting_comparision.txt", "w") as f:
        #f.write("Input_size sel_sort bubble_sort quick_sort merge_sort insertion_sort\n")
        for i in input_sizes:
            array = random.sample(range(0,10000000,100),i)
            f.write(str(i)+" "+str(find_time(sel_sort, array, i))+" "+str(find_time(bubble_sort, array, i))+" "+str(find_time(quick_sort, array, i))+" "+str(find_time(merge_sort, array, i))+" "+str(find_time(ins_sort, array, i))+" "+str(find_time(dcs, array, i))+"\n")

def find_time(fun, array, i):
	if fun == quick_sort:
		start = time.time()
		fun(array, 0, i-1)
		end = time.time()
	else:
		start = time.time()
		fun(array, i)
		end = time.time()
	return log(1+ (end-start))

def pyth_plot():
    input_size=random.sample(range(10,3000),50)
    input_size.sort()
    df = {'input_size':[], 'quick_sort':[], 'merge_sort':[], 'sel_sort': [], 'bubble_sort':[], 'ins_sort':[]}
    for i in input_size:
        array = random.sample(range(0,1000000,100),i)
        df['input_size'].append(i)
        df['merge_sort'].append(find_time(merge_sort, array, i))
        df['quick_sort'].append(find_time(quick_sort, array, i))
        df['sel_sort'].append(find_time(sel_sort, array, i))
        df['ins_sort'].append(find_time(ins_sort, array, i))
        df['bubble_sort'].append(find_time(bubble_sort, array, i))
    df = pd.DataFrame.from_dict(df)
    #print(df)
    sns.lineplot(data=df.iloc[:,1:])
    plt.show()

def gnu_plot():
    input_size=random.sample(range(10,1000),50)
    input_size.sort()
    analyze(input_size)
    gnu_YES = '''
        set xlabel "Size of Input"
        set ylabel "Time Taken"
        set title "Graph"
        set style line 1 lc rgb "#ff0000" lt 1 lw 0.8 pt 1 ps 0.4
        set style line 2 lc rgb "#00a066" lt 1 lw 0.8 pt 1 ps 0.4
        set style line 3 lc rgb "#0f4080" lt 1 lw 0.8 pt 1 ps 0.4
        set style line 4 lc rgb "#90ff00" lt 1 lw 0.8 pt 1 ps 0.4
        set style line 5 lc rgb "#100288" lt 1 lw 0.8 pt 1 ps 0.4
        set style line 6 lc rgb "#ef00ff" lt 1 lw 0.8 pt 1 ps 0.4
        plot "sorting_comparision.txt" using 1:2 with linespoints ls 1 title "Selection Sort", '' using 1:3 with linespoints ls 2 title "Bubble Sort", '' using 1:4 with linespoints ls 3 title "Quick Sort", '' using 1:5 with linespoints ls 4 title "Merge Sort", '' using 1:6 with linespoints ls 5 title "Insertion Sort", '' using 1:7 with linespoints ls 6 title "Distribution CS"
        set term png
        set output "outputimage.png"
        replot
    '''
    with open('plot.gnu','w') as p: p.write(gnu_YES);
    system("gnuplot -persist plot.gnu")

if __name__ == '__main__':
	gnu_plot()
	#pyth_plot()



