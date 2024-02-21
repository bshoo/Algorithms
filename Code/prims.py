#!/usr/bin/env python3

def prim(graph):
    vt = [list(graph.keys())[0]]
    et = []
    for i in range(len(graph)-1):
        min_edge = find_min(graph, vt)
        if min_edge is None:
            break
        vt.append(min_edge[1])
        et.append(min_edge)
    return et

def find_min(graph, vt):
    min_d = 999999
    min_ed = None
    #print(vt)
    for v in vt:
        for u in graph[v]:
            if u not in vt and graph[v][u] < min_d:
                min_d = graph[v][u]
                min_ed = v, u
    return min_ed

def input_graph():
    g = {}
    for i in range(int(input("Enter number of edges "))):
        print(f"\nEdge: {i}\n")
        src = input(f"\nEnter source ")
        dest = input("Enter adjacent node ")
        weight = int(input("Enter edge weight "))

        if src not in g:
            g[src] = {}
        g[src][dest] = weight

        if dest not in g:
            g[dest] = {}
        g[dest][src] = weight
    #print(g)
    return g

print("\nEdge set of Minimum spanning Tree using Prim's: ",prim(input_graph()))

