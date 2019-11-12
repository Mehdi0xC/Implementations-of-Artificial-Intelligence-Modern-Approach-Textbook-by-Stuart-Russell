from result import Result
import queue
from node import Node
from problem import Problem

class Search(object):
    def __init__(self,problem):
        self.problem = problem
        self.result = Result("N/A")


    def IDFS(self,maxDepth):
        for depth in range(1,maxDepth):
            self.frontiers = queue.LifoQueue()
            self.explored = []
            self.frontiers.put(Node(self.problem.initialState , None , "Nothing" , 0))
            while(True):
                if(self.frontiers.empty()):
                    self.result.changeStatus("Failure")
                    self.result.expandedNodes = self.problem.expandedNodes
                    self.result.depth = depth
                    return self.result
                leaf = self.frontiers.get()
                self.explored.append(leaf.state)
                self.problem.expand(leaf.state)
                for i in range(len(self.problem.nextStates)):
                    child = Node(self.problem.nextStates[i] , leaf , self.problem.nextAction[i] , leaf.depth+1)
                    if((child.state not in self.explored)and(child not in list(self.frontiers.queue))and(child.depth<=depth)):
                        if(child.state in self.problem.finalStates):
                            self.result.changeStatus("Success")
                            while(child.parent != None):
                                self.result.addToPath(child.action)
                                child = child.parent
                            self.result.expandedNodes = self.problem.expandedNodes
                            self.result.depth = depth
                            return self.result
                        self.frontiers.put(child)
