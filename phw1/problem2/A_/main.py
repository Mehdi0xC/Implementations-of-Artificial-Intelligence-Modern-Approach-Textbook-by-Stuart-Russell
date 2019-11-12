from node import Node
from problem import Problem
from search import Search


problem = Problem([1,2,5,3,4,0,6,7,8])
# problem.randomInitialStateGenerator()
s = Search(problem)
r = s.A_Star_Search()
r.path.reverse()
print(r.path)
