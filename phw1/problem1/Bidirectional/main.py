from node import Node
from problem import Problem
from search import Search

p = Problem()
s = Search(p)

# path = s.BFS().path
# path.reverse()
R = s.BiDirectional()
print(R.path)
