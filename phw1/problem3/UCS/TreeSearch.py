from queue import LifoQueue as LIFO
import queue
from node import Node
from result import Result

class TreeSearch(object):
    def __init__(self, problem):
        self.problem = problem
        self.result = Result("N/A")



    def getNodeWithMinimumCost(self,frontiers):
        minimumLeaf = frontiers[0]
        for node in frontiers :
            if (node.costFromStart) <= (minimumLeaf.costFromStart) :
                minimumLeaf = node
        return minimumLeaf



    def UCS_Search(self):
        self.frontiers = []
        self.explored = []
        self.frontiers.append(Node(self.problem.initialState , None , "None" , 0 ))
        while(True) :
            if len(self.frontiers)==0 :
                self.result.changeStatus("Failure")
                return self.result
            leaf = self.getNodeWithMinimumCost(self.frontiers)
            self.frontiers.remove(leaf)
            self.explored.append(leaf.data)
            self.problem.expand(leaf.data)
            for i in range(len(self.problem.nextStates)) :
                child = Node(self.problem.nextStates[i] , leaf , self.problem.nextAction[i] , leaf.costFromStart+1 )
                if (not((child.data in self.explored)) and (child not in self.frontiers)):
                    leaf.append(child)
                    if (child.data in self.problem.finalStates):
                        print(child.data)
                        self.result.changeStatus("Success")
                        while(child.data != self.problem.initialState):
                            self.result.addToPath(child.action)
                            child = child.parent
                        return self.result
                    self.frontiers.append(child)
