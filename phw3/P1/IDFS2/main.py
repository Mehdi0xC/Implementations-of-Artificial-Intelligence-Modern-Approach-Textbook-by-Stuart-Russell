from node import Node
from problem import Problem
from search import Search


p = Problem()
s = Search(p)

i = 2
while(s.DFS(i).status != "Success"):
    print(s.DFS(i).status + " at depth : " + str(i-1))
    i=i+1
    if(i > 100):
        print("No answer till depth 100")
        break
print(s.DFS(i).status + " at depth : " + str(i-1))
r = s.DFS(i)
path = r.path
path.reverse()
print(path)
print("number of visited : ")
print (r.expandedNodes)
print("number of expansions : ")
print (r.expansions)
print("depth : ")
print (r.depth)


# print(r.status)
# path = r.path
# path.reverse()
# print(path)
# print("number of expansions : ")
# print (r.expandedNodes)
# print("depth : ")
# print (r.depth)
