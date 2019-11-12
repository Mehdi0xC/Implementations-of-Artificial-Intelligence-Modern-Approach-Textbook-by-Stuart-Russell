import time as t
import random as rnd
import numpy as np
class Algorithm(object):
    def __init__(self,problem):
        self.problem = problem



    def SA(self , mode=0 , runningTime=10 , simulatedAnnealingTrials=10000):
        trials = simulatedAnnealingTrials
        annealingFunction = []
        if(mode == 0):
            for i in range(2,trials+2):
                annealingFunction.append(1/i)
        elif(mode == 1):
            difference = 1/trials
            distance = 1
            while distance > 0:
                distance = distance - difference
                annealingFunction.append(distance)
        elif(mode == 2):
            for i in range(1,trials+1):
                annealingFunction.append(1/2*i)

        currentState = self.problem.state
        currentCost = self.problem.getCost(currentState)
        tick = t.clock()
        tock = t.clock()
        trial = 1
        while(tock - tick < runningTime):
            nextState = self.problem.nextStateGenerator(currentState)
            p = rnd.random()
            if self.problem.getCost(nextState) < self.problem.getCost(currentState) :
                if(trial < trials and p > annealingFunction[trial]) :
                    currentState = nextState
            else :
                if(trial < trials and p < annealingFunction[trial]) :
                    currentState = nextState
            if(trial >= trials)  :
                    currentState = nextState
            trial = trial + 1
            tock = t.clock()
        return [currentState,self.problem.getCost(currentState)]
