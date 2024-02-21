#!/usr/bin/env python3

def input_graph():
    g = {}
    sorted_edgelist = {}
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
        
        sorted_edgelist[tuple(set((src,dest)))]=weight

    print(g)
    print("\n",sorted_edgelist)
    return g, sorted(sorted_edgelist, key=sorted_edgelist.get)

#print(input_graph())

def find_parent(u):
    if parent[u] != u:
        return find_parent(parent[u])
    return u


def find_mst(graph, wlist):
    n = len(graph)-1
    et = []
    #parent = {i:i for i in g}
    # USE RANK BRO
    for edge in wlist:
        i = find_parent(edge[0])
        j = find_parent(edge[1])
        if i==j:
            continue
        elif i == edge[0] and j!=edge[1]:
            parent[i] = edge[1]
        elif i != edge[0] and j == edge[1]:
            parent[j] = edge[0]
        else:
            parent[edge[0]] = edge[1]
        et.append(edge)
        if len(et) == n:
            break
    return et


g, wlist = input_graph()
parent = {i:i for i in g}
print(find_mst(g, wlist))
