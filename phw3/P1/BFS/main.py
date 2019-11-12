from node import Node
from problem import Problem
from search import Search


p = Problem()
s = Search(p)
r = s.BFS()

print(r.status)
path = r.path
path.reverse()
print(path)
print("number of visited : ")
print (r.expandedNodes)
print("number of expansions : ")
print (r.expansions)
