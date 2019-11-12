import time as t
import random as rnd
import numpy as np
class algorithm(object):
    def __init__(self,problem):
        self.problem = problem


    def stochasticHillClimbingSearch(self,runningTime=10):
        currentState = self.problem.state
        currentCost = self.problem.getCost(currentState)
        print("Current state is :")
        self.problem.printX(currentState)
        print("Current cost is :")
        print(self.problem.getCost(currentState))
        tic = t.clock()
        while(currentCost != 0):
            betterNextStates = []
            nextStates = self.problem.nextStatesGenerator(currentState)
            for state in nextStates:
                if self.problem.getCost(state) < self.problem.getCost(currentState):
                        betterNextStates.append(state)
            toc = t.clock()
            if(len(betterNextStates) != 0):
                randomNumber = np.random.randint(0,len(betterNextStates))
                currentState = betterNextStates[randomNumber]
            if (toc - tic > runningTime):
                break;
        print("Final state is :")
        self.problem.printX(currentState)
        print("Final cost is :")
        print(self.problem.getCost(currentState))


    def firstBestHillClimbingSearch(self,runningTime=10):
        currentState = self.problem.state
        currentCost = self.problem.getCost(currentState)
        print("Current state is :")
        self.problem.printX(currentState)
        print("Current cost is :")
        print(self.problem.getCost(currentState))
        tic = t.clock()
        while(currentCost != 0):
            nextState= self.problem.nextStateGenerator(currentState)
            if self.problem.getCost(nextState) < self.problem.getCost(currentState):
                currentState = nextState
            toc = t.clock()
            if (toc - tic > runningTime):
                break;
        print("Final state is :")
        self.problem.printX(currentState)
        print("Final cost is :")
        print(self.problem.getCost(currentState))


    def randomRestartHillClimbingSearch(self,runningTime=10):
        restarts = 0
        currentState = self.problem.state
        stuckList = []
        currentCost = self.problem.getCost(currentState)
        print("Current state is :")
        self.problem.printX(currentState)
        print("Current cost is :")
        print(self.problem.getCost(currentState))
        tic = t.clock()
        while(currentCost != 0):
            betterNextStates = []
            nextStates = self.problem.nextStatesGenerator(currentState)
            for state in nextStates:
                if self.problem.getCost(state) < self.problem.getCost(currentState):
                        betterNextStates.append(state)
            stuckList.append(currentCost)
            toc = t.clock()
            if (stuckList.count(currentCost) >= 4):
                restarts = restarts + 1
                currentState = self.problem.makeRandomState(currentState)
            if(len(stuckList) == 20):
                stuckList.clear()
            if (toc - tic > runningTime):
                break;
        print("Final state is :")
        self.problem.printX(currentState)
        print("Final cost is :")
        print(self.problem.getCost(currentState))
        print("number of restarts :")
        print(restarts)
