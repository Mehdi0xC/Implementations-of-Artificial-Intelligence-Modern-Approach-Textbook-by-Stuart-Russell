from result import Result
import queue
from node import Node
from problem import Problem

class Search(object):
    def __init__(self,problem):
        self.problem = problem
        self.result = Result("N/A")


    def BFS(self):
        self.frontiers = queue.Queue()
        self.explored = []
        self.frontiers.put(Node(self.problem.initialState , None , "Nothing"))
        j = 0
        while(True):
            j = j+1
            print(j)
            if(self.frontiers.empty()):
                self.result.changeStatus("Failure")
                return self.result
            leaf = self.frontiers.get()
            #print(leaf.state)
            self.explored.append(leaf.state)
            self.problem.expand(leaf.state)
            for i in range(len(self.problem.nextStates)):
                child = Node(self.problem.nextStates[i] , leaf , self.problem.nextAction[i])
                # print(child.state)
                if((child.state not in self.explored)and(child not in list(self.frontiers.queue))):
                    if(child.state in self.problem.finalStates):
                        self.result.changeStatus("Success")
                        while(child.parent != None):
                            self.result.addToPath(child.action)
                            child = child.parent
                        return self.result
                    self.frontiers.put(child)


   