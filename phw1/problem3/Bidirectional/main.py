from problem import Problem0
from search import Search


field = [[1,1,0,0],[0,1,1,1],[1,1,1,1],[1,1,1,1]]
p = Problem0(4,4,field)
search = Search(p)
r = search.BiDirectional()
print(r.path)
