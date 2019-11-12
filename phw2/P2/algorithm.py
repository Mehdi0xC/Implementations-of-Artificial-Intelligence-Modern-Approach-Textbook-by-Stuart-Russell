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
        mainState = self.problem.state
        randomNumber = int(np.floor(rnd.random()*self.problem.population))
        currentSubGraph0 = list(set(rnd.choices(mainState,k=randomNumber)))
        currentSubGraph1 = list(set(mainState)-set(currentSubGraph0))
        costSoFar = self.problem.getCost(currentSubGraph0,currentSubGraph1)
        costSoFar = self.problem.getCost(currentSubGraph0,currentSubGraph1)
        tick = t.clock()
        tock = t.clock()
        trial = 1
        while(tock - tick < runningTime):
            randomNumber = int(np.floor(rnd.random()*self.problem.population))
            subGraph0 = list(set(rnd.choices(mainState,k=randomNumber)))
            subGraph1 = list(set(mainState)-set(subGraph0))
            cost = self.problem.getCost(subGraph0,subGraph1)
            if cost < costSoFar :
                p = rnd.random()
                if(trial < trials and p > annealingFunction[trial]) :
                    currentSubGraph0 = subGraph0
                    currentSubGraph1 = subGraph1
                    costSoFar = cost
                if(trial >= trials)  :
                    currentSubGraph0 = subGraph0
                    currentSubGraph1 = subGraph1
                    costSoFar = cost
            trial = trial + 1
            tock = t.clock()
        return [currentSubGraph0 , currentSubGraph1]
