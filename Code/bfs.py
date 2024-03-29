nodes = {0:[1, 3],1:[0,3,5],2:[4, 6],3:[1, 0, 5, 7],4:[7, 6, 2],5:[1, 3, 6],6:[2, 4, 5, 7],7:[4, 6, 3]}
visited = []
queue = []

def BFS():
  for node in nodes:
    if node not in visited:
      bfs(node)

def bfs(n):
  visited.append(n)
  queue.append(n)
  while len(queue)!=0:
    for w in sorted(nodes[queue[0]]):
      if w not in visited:
        visited.append(w)
        queue.append(w)
      del queue[0]

BFS()
print("BFS: ",visited)
