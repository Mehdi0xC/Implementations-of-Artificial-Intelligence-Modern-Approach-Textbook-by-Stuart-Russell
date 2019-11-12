from result import Result
import queue
from node import Node
from problem import Problem

class Search(object):
    def __init__(self,problem):
        self.problem = problem
        self.result = Result("N/A")

    def BFS(self , graphSearch=None):
        """BFS Search"""
        if(graphSearch != None):
            self.frontiers = queue.Queue()
            self.explored = []
            self.frontiers.put(Node(self.problem.initialState , None , "Nothing"))
            while(True):
                if(self.frontiers.empty()):
                    self.result.changeStatus("Failure")
                    self.result.expandedNodes = self.problem.expandedNodes
                    return self.result
                leaf = self.frontiers.get()
                self.explored.append(leaf.state)
                self.problem.expand(leaf.state)
                self.result.expansions = self.result.expansions + 1
                for i in range(len(self.problem.nextStates)):
                    child = Node(self.problem.nextStates[i] , leaf , self.problem.nextAction[i])
                    leaf.addChild(child)
                    if((child.state not in self.explored)and(child not in list(self.frontiers.queue))):
                        if(child.state in self.problem.finalStates):
                            self.result.changeStatus("Success")
                            while(child.parent != None):
                                self.result.addToPath(child.action)
                                child = child.parent
                            self.result.expandedNodes = self.problem.expandedNodes
                            return self.result
                        self.frontiers.put(child)
                        if(len(list(self.frontiers)) >= self.result.maxFrontiers):
                            self.result.maxFrontiers = len(list(self.frontiers))
        else:
            self.frontiers = queue.Queue()
            self.frontiers.put(Node(self.problem.initialState , None , "Nothing"))
            while(True):
                if(self.frontiers.empty()):
                    self.result.changeStatus("Failure")
                    self.result.expandedNodes = self.problem.expandedNodes
                    return self.result
                leaf = self.frontiers.get()
                self.problem.expand(leaf.state)
                self.result.expansions = self.result.expansions + 1
                for i in range(len(self.problem.nextStates)):
                    child = Node(self.problem.nextStates[i] , leaf , self.problem.nextAction[i])
                    leaf.addChild(child)
                    if((child not in list(self.frontiers.queue))):
                        if(child.state in self.problem.finalStates):
                            self.result.changeStatus("Success")
                            while(child.parent != None):
                                self.result.addToPath(child.action)
                                child = child.parent
                            self.result.expandedNodes = self.problem.expandedNodes
                            return self.result
                        self.frontiers.put(child)
