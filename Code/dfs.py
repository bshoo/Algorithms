#!/usr/bin/env python3

nodes = {}
while True:
    node = input("Enter name of node ")
    nodes[node]:[]
    adj = input("Enter adjacent nodes with spaces ")
    nodes[node] = adj.split()
    if input("Do you want to continue?[y/n] ").upper() == 'N':
        break

visited = []
def DFS():
    for node in sorted(nodes.keys()):
        if node not in visited:
            dfs(node)

def dfs(n):
    visited.append(n)
    for node in sorted(nodes[n]):
        if node not in visited:
            dfs(node)
DFS()
print(visited)
