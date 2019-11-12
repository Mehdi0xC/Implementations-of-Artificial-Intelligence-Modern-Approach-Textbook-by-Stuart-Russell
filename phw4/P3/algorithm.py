import time as t
import random as rnd
import numpy as np
from copy import deepcopy as cp
import matplotlib.pyplot as plt

class Algorithm(object):
    def __init__(self,problem,mutationRate,crossOverRate,trials):
        self.problem = problem
        self.mutationRate = mutationRate
        self.crossOverRate = crossOverRate
        self.trials = trials


    def genetics(self):
        trial = 0
        bestCosts = []
        worstCosts = []
        avgCosts = []
        chromosomes = self.problem.makeFirstChromosomes()
        while(trial<self.trials):
            evaluationVector = self.evaluation(chromosomes)
            fitnessVector = self.fitness(evaluationVector)
            probabilityVector = self.probabilities(fitnessVector)
            wheelVector = self.wheel(probabilityVector)
            parents = self.selectParents(wheelVector,self.crossOverRate,chromosomes)
            chromosomes = self.crossOver(parents)
            chromosomes = self.mutation(chromosomes,self.mutationRate)
            trial = trial+1
            costVector = self.costs(chromosomes)
            bestCosts.append(np.min(costVector))
            worstCosts.append(np.max(costVector))
            avgCosts.append(np.average(costVector))
        plt.plot(bestCosts,'g',worstCosts,'r',avgCosts,'b')
        plt.show()
        return chromosomes


    def evaluation(self,chromosomes):
        evaluationVector = []
        for chromosome in chromosomes:
            evaluationVector.append(self.problem.getCost(chromosome))
        return evaluationVector

    def fitness(self,evaluationVector):
        fitnessVector = []
        for i in range (0,len(evaluationVector)):
            fitnessVector.append(1/(1+evaluationVector[i]))
        return fitnessVector

    def probabilities(self,fitnessVector):
        probabilityVector = []
        total = 0
        for i in fitnessVector:
            total = total + i
        for i in range (0,len(fitnessVector)):
            probabilityVector.append(fitnessVector[i]/total)
        return probabilityVector


    def wheel(self,probabilityVector):
        wheelVector = []
        ruler = 0
        for probability in probabilityVector:
            wheelVector.append([ruler,ruler + probability])
            ruler = ruler + probability
        return wheelVector

    def selectParents(self,wheelVector,crossOverRate,chromosomes):
        parents = []
        parentsCount = int(np.floor(self.problem.population*self.crossOverRate))
        for i in range(0,parentsCount):
            p = np.random.rand()
            for i in range(len(wheelVector)):
                if((wheelVector[i][0] < p) and (p <= wheelVector[i][1])):
                    parents.append(chromosomes[i])
        return parents

    def crossOver(self,parents):
        newGeneration = []
        randomParent0 = np.random.randint(0,len(parents))
        randomParent1 = np.random.randint(0,len(parents))
        for i in range(self.problem.population):
            newGeneration.append(self.problem.combine(parents[randomParent0],parents[randomParent1]))
        return newGeneration

    def mutation(self,chromosomes,mutationRate):
        numberOfMutations = int(np.floor(self.problem.population*mutationRate))
        choosenForMutation = []
        for i in range (0 , numberOfMutations):
            chromosomes[i] = self.problem.mutate(chromosomes[i])
        return chromosomes

    def costs(self,chromosomes):
        costVector = []
        for chromosome in chromosomes:
            costVector.append(self.problem.getCost(chromosome))
        return costVector
