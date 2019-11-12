from node import Node
from problem import Problem
from search import Search


p = Problem()
s = Search(p)
r = s.IDFS(maxDepth=14)

print(r.status)
path = r.path
path.reverse()
print(path)
print("number of expansions : ")
print (r.expandedNodes)
print("depth : ")
print (r.depth)
