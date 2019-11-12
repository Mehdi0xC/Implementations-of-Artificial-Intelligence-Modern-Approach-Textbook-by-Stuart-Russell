from node import Node
from problem import Problem
from search import Search
from result import Result

p = Problem()
s = Search(p)
r = s.Astar()

print(r.status)
path = r.path
path.reverse()
print(path)
print("number of expansions : ")
print (r.expandedNodes)
