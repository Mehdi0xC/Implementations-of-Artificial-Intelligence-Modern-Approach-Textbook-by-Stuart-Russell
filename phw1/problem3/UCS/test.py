from problem import Problem0
from TreeSearch import TreeSearch


field = [[1,1,0,0],[0,1,1,1],[1,1,1,1],[1,1,1,1]]
p = Problem0(4,4,field)
search = TreeSearch(p)
r = search.UCS_Search()
r.path.reverse()
print(r.path)
