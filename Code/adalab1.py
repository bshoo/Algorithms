#!/usr/bin/env python3

import random
import sys
import time
from os import system
'''Shashank B Sharma, pes1pg22ca184 '''

def sel_sort(inp):
    n = len(inp)
    for i in range(n-1,0,-1):
        mini = i
        for j in range(i):
            if inp[j] > inp[mini] : mini = j
        if mini != i:
            x = inp[i]
            inp[i] = inp[mini]
            inp[mini]=x
    #print(inp)
#sel_sort([2,1,33,44,11,2,50])

def seq_search(inp):
	l = len(inp)
	key = 1
	inp.append(key)
	i = 0
	while inp[i] != key:
		i += 1
	if i==l:
		return
	else:
		return

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
	    for j in range(0, n-i-1):
		    if arr[j] > arr[j+1]:
			    arr[j], arr[j+1] = arr[j+1], arr[j]

'''
def quick_sort(ar,l,r):
    if l<r:
        s = partition(ar,l,r)
        quick_sort(ar,l,s-1)
        quick_sort(ar,s+1,r)
#ERRORRR
def partition(ar,l,r):
    p = ar[l]
    i = l; j = r
    while i < j:
        while i!=j and ar[i] >= p:
            i+=1
        while i!=j and ar[j] <= p: 
            j -= 1
        ar[i],ar[j] = ar[j],ar[i]

    ar[i],ar[j] = ar[j],ar[i]
    ar[l],ar[j] = ar[j],ar[l]
    return j+1
'''

def quick_sort(ar, l, r):
    if l < r:
        s = partition(ar, l, r)
        quick_sort(ar, l, s - 1)
        quick_sort(ar, s + 1, r)

def partition(ar, l, r):
    p = ar[l]
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

def ins_sort(a):
    n = len(a)
    for i in range(1, n):
        v = a[i]
        j = i-1
        while j>=0 and a[j] > v:
            a[j+1] = a[j]
            j-=1
        a[j+1] = v

def bsearch(arr, key, l, h):
    mid = int((l+h)/2)
    if l>h:
        return -1
    elif arr[mid] == key:
        return mid+1
    elif key>arr[mid]:
        return bsearch(arr, key, mid+1, h)
    else:
        return bsearch(arr, key, l, mid-1)



def analyze(func, input_size, n):
    with open("plot_data.txt","w") as pf:
        for i in input_size:
            arr = random.sample(range(100,1000*n,100),i)
            start = time.time()
            func(arr)
            end = time.time()
    
            pf.write(str(i)+" "+str((end-start) * 10000000)+" "+str(i*i)+"\n")
            


def plot(function = bubble_sort, n=100):
	'''Shashank B Sharma, pes1pg22ca184 '''	
	gnuplot_script = '''
	set xlabel "Input Size"
	set ylabel "Time Tken (seconds)"
	set title "Time efficiency of Sequential Search"
	set style line 1 lc rgb '#000000' lt 2 lw 2 pt 11 ps 0.5
	set style line 2 lc rgb '#ff0000' lt 2 lw 2 pt 13 ps 0.5
	plot "plot_data.txt" u 1:2 w lp pt 1 title 'Actual Time', '' u 1:3 w lp pt 1 title 'Estimated Time'
	set term png
	set output sort_efficiency.png
	OT_QPA_PLATFORM=wayland
	replot
	'''
	gnu = """set xlabel 'X'\n
	set ylabel 'Y'\n
	set title 'Graph'\n
	set style line 1 lc rgb '#ff0000' lt 1 lw 5 pt 15 ps 5\n
	set style line 2 lc rgb '#000000' lt 1 lw 5 pt 15 ps 5\n
	plot "plot_data.txt" using 1:2 with lines title 'Legend 1', '' using 1:3 with lines title 'Legend 2'\n
	set terminal png\n
	set output 'outputimage.png'\n
	replot\n
	"""
	gnu_YES = '''
        set xlabel "X"
        set ylabel "Y"
        set title "Graph"
        set style line 1 lc rgb "#ff0000" lt 1 lw 2 pt 4 ps 0.4
        set style line 2 lc rgb "#000000" lt 1 lw 2 pt 4 ps 0.4
        plot "plot_data.txt" using 1:2 with linespoints ls 1 title "Legend 1", '' using 1:3 with linespoints ls 2 title "Legend 2"
        set term png
        set output "outputimage.png"
        replot
	'''
	try:
		n = int(sys.argv[1]) # the number of random values needed
		input_size=random.sample(range(10,10*n),n) #This is the sizes of the inputs to be given, array of input sizes
		input_size.sort()
	except:
		print("No arguments given")
		exit(0)
	analyze(function, input_size, n);
	with open('plot.gnu','w') as p: p.write(gnu_YES);
	system("gnuplot -persist plot.gnu")
	
if __name__=='__main__':
    try:
        plot(sys.argv[2], sys.argv[1])
    except:
        plot()
