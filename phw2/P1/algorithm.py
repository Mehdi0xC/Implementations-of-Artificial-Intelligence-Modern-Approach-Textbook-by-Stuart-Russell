import time as t
import random as rnd
class algorithm(object):
    def __init__(self,problem):
        self.problem = problem

    def randomRestartHillClimbingSearch(self,runningTime=10,maxRestarts=10):
        restarts = 0
        currentState = self.problem.makeState()
        # currentState = [[0, 0, 0, 1, 0, 0, 0, 0] ,
        #                 [0, 0, 0, 0, 1, 0, 0, 0] ,
        #                 [0, 0, 0, 0, 0, 0, 0, 1] ,
        #                 [0, 1, 0, 0, 0, 0, 0, 0] ,
        #                 [0, 0, 0, 0, 0, 0, 1, 0] ,
        #                 [1, 0, 0, 0, 0, 0, 0, 0] ,
        #                 [0, 0, 1, 0, 0, 0, 0, 0] ,
        #                 [0, 0, 0, 0, 1, 0, 0, 0]]
        stuckList = []
        currentCost = self.problem.getCost(currentState)
        print("Current state is :")
        self.problem.printX(currentState)
        print("Current cost is :")
        print(self.problem.getCost(currentState))
        tic = t.clock()
        while(currentCost != 0):
            nextStates = self.problem.nextStatesGenerator(currentState)
            betterState = nextStates[0]
            for state in nextStates:
                if self.problem.getCost(state) < self.problem.getCost(betterState):
                    betterState = state
            currentState = betterState
            currentCost = self.problem.getCost(currentState)
            stuckList.append(currentCost)
            toc = t.clock()
            print("Current state is :")
            self.problem.printX(currentState)
            print("Current cost is :")
            print(self.problem.getCost(currentState))
            if (stuckList.count(currentCost) >= 10):
                restarts = restarts + 1
                currentState = self.problem.makeState()
                print("RESTARTING FOR " + str(restarts) + " TIME!")
            if(len(stuckList) == 20):
                stuckList.clear()
            if (toc - tic > runningTime):
                break;
            if(restarts >= maxRestarts):
                break;
        self.problem.printX(currentState)
        print("Final cost is :")
        print(self.problem.getCost(currentState))
        print("number of restarts :")
        print(restarts)
