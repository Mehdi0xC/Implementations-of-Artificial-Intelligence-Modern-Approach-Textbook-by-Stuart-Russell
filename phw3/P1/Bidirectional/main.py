from node import Node
from problem import Problem
from search import Search
from result import Result

p = Problem()
s = Search(p)
r = s.BiDirectional()

print(r.status)
path = r.path
print(path)
print("number of visited : ")
print (r.expandedNodes)
print("number of expansions : ")
print (r.expansions)
