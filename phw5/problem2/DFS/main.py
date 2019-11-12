from node import Node
from problem import Problem
from search import Search


p = Problem()
s = Search(p)
r = s.DFS(graphSearch=True)

print(r.status)
path = r.path
path.reverse()
print(path)
print("number of expansions : ")
print (r.expandedNodes)
