from result import Result
import queue
from node import Node
from problem import Problem

class Search(object):
    def __init__(self,problem):
        self.problem = problem
        self.result = Result("N/A")



    def BiDirectional(self):
        self.initialFrontiers = queue.Queue()
        self.initialExplored = []
        self.goalFrontiers = queue.Queue()
        self.goalExplored = []
        self.initialFrontiers.put(Node(self.problem.initialState , None , "Nothing"))
        dummyParent = Node("dummy" , None , "Nothing")
        for goalState in self.problem.finalStates :
            goal = Node(goalState , dummyParent , "Nothing")
            dummyParent.addChild(goal)
        for goalState in dummyParent.children:
            self.goalFrontiers.put(goalState)
        while(self.result.status  == "N/A"):
            self.initialExpansion()
            self.goalExpansion()
        return self.result





    def initialExpansion(self):
        if(self.initialFrontiers.empty()):
            self.result.changeStatus("Failure")
            return self.result
        leaf = self.initialFrontiers.get()
        self.initialExplored.append(leaf.state)
        self.problem.expand(leaf.state)
        for i in range(len(self.problem.nextStates)):
            child = Node(self.problem.nextStates[i] , leaf , self.problem.nextAction[i])
            if((child.state not in self.initialExplored)and(child not in list(self.initialFrontiers.queue))):
                for goal in list(self.goalFrontiers.queue):
                    if(child.state == goal.state):
                        self.result.changeStatus("Success")
                        while(child.parent != None):
                            self.result.path.append(child.action)
                            print(child.state)
                            child = child.parent
                        self.result.path.reverse()
                        print(self.result.path)
                        while(goal.state != "dummy"):
                            self.result.path.append(self.problem.flipAction(goal.action))
                            print(goal.state)
                            goal = goal.parent
                        print("succeeees")
                        print(goal.state)
                        return self.result
                self.initialFrontiers.put(child)

    def goalExpansion(self):
        if(self.goalFrontiers.empty()):
            self.result.changeStatus("Failure")
            return self.result
        leaf = self.goalFrontiers.get()
        self.goalExplored.append(leaf.state)
        self.problem.expand(leaf.state)
        for i in range(len(self.problem.nextStates)):
            child = Node(self.problem.nextStates[i] , leaf , self.problem.nextAction[i])
            if((child.state not in self.goalExplored)and(child not in list(self.goalFrontiers.queue))):
                self.goalFrontiers.put(child)
