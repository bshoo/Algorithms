#!/usr/bin/env python3

def bottomup(heap):
    n = len(heap)-1
    for i in range(int(n/2),0,-1):
        k = i; v = heap[k]
        heaped = False
        while not heaped and (k*2) <= n:
            j = k*2
            if j < n:
                if heap[j] < heap[j+1]:
                    j += 1
            if v >= heap[j]:
                heaped = True
            else:
                heap[k] = heap[j]
                k = j
        heap[k] = v


arr = [69,1,2,3,4,5,6,7]
print("Heap: ",arr)
bottomup(arr)
print("Heaped heap: ",arr)

