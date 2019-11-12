import time as t
import random as rnd
import numpy as np
from copy import deepcopy as cp
import matplotlib.pyplot as plt

class Algorithm(object):
    def __init__(self,problem):
        self.problem = problem
        self.answers = []
        self.realAnswers = []

    def genetics(self,crossOverRate = 0.4,mutationRate=0.01,trials=1000):
        trial = 0
        bestCosts = []
        worstCosts = []
        avgCosts = []
        chromosomes = self.makeFirstChromosomes()
        while(trial<trials):
            evaluationVector = self.evaluation(chromosomes)
            fitnessVector = self.fitness(evaluationVector)
            probabilityVector = self.probabilities(fitnessVector)
            wheelVector = self.rouletteWheel(probabilityVector)
            randomVector = self.randomizer(wheelVector)
            chromosomes = self.nextGeneration(wheelVector,randomVector,chromosomes)
            parentsData = self.selectParents(crossOverRate,chromosomes)
            chromosomes = self.crossOver(parentsData,chromosomes)
            chromosomes = self.mutation(chromosomes,mutationRate)
            trial = trial+1
            costVector = self.costs(chromosomes)
            bestCosts.append(np.min(costVector))
            worstCosts.append(np.max(costVector))
            avgCosts.append(np.average(costVector))
        plt.plot(bestCosts,'g',worstCosts,'r',avgCosts,'b')
        plt.show()
        return chromosomes

    def makeFirstChromosomes(self):
        chromosomes = []
        for i in range(0,self.problem.population) :
            terms = []
            for j in range(0,self.problem.equationTerms):
                terms.append(int(np.floor(((self.problem.constantNumber)/self.problem.factors[j])*rnd.random())))
            chromosomes.append(terms)
        return chromosomes

    def evaluation(self,chromosomes):
        evaluationVector = []
        for c in chromosomes:
            x = 0
            for i in range (0,self.problem.equationTerms):
                x = x + self.problem.factors[i]*c[i]
            if(x == self.problem.constantNumber):
                self.answers.append(c)
            evaluationVector.append(abs(x-self.problem.constantNumber))
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

    def rouletteWheel(self,probabilityVector):
        wheelVector = []
        for i in range(0,len(probabilityVector)):
            x = 0
            for j in range(0,i+1):
                x = x + probabilityVector[j]
            wheelVector.append(x)
        return wheelVector

    def randomizer(self,wheelVector):
        randomVector = []
        for i in range(0,len(wheelVector)):
            randomVector.append(rnd.random())
        return randomVector

    def nextGeneration(self,wheelVector,randomVector,chromosomes):
        newChromosomes = []
        for p in range(len(randomVector)):
            for i in range(0,len(wheelVector)):
                if randomVector[p] < wheelVector[i] :
                    newChromosomes.append(chromosomes[i])
                    break
        return newChromosomes

    def selectParents(self,crossOverRate,chromosomes):
        parents = []
        parentNumbers = []
        while(len(parents) == 0):
            for i in range(0,len(chromosomes)):
                if (rnd.random() < crossOverRate):
                    parents.append(chromosomes[i])
                    parentNumbers.append(i)
        return [parents,parentNumbers]

    def crossOver(self,parentsData,inputChromosomes):
        chromosomes = inputChromosomes
        parents = parentsData[0]
        parentNumbers = parentsData[1]
        for i in range(0,len(parents)-1) :
            randomNumber = 0
            while(randomNumber == 0):
                randomNumber = int(np.floor(rnd.random()*self.problem.equationTerms))
            chromosomes[parentNumbers[i]] = self.combine(parents[i],parents[i+1],randomNumber)
        randomNumber = 0
        while(randomNumber == 0):
            randomNumber = int(np.floor(rnd.random()*self.problem.equationTerms))
        chromosomes[parentNumbers[len(parents)-1]] = self.combine(parents[len(parents)-1] , parents[0] , randomNumber)
        return chromosomes


    def combine(self,chromosome0 , chromosome1 , cutPoint):
        child = chromosome0[0:cutPoint] + chromosome1[cutPoint:len(chromosome1)]
        return child


    def mutation(self,inputChromosomes,mutationRate):
        chromosomes = inputChromosomes
        gens = len(chromosomes) * len(chromosomes[0])
        numberOfMutations = int(np.floor(gens*mutationRate))
        for i in range (0 , numberOfMutations):
            x = int(np.floor(rnd.random()*len(chromosomes)))
            y = int(np.floor(rnd.random()*len(chromosomes[0])))
            z = int(np.floor(rnd.random()*(((self.problem.constantNumber)/(self.problem.factors[y]))+1)))
            chromosomes[x][y] = z
        return chromosomes


    def costs(self,chromosomes):
        costVector = []
        for chromosome in chromosomes :
            cost = 0
            for i in range(len(chromosome)) :
                cost = cost + chromosome[i]*self.problem.factors[i]
            costVector.append(abs(cost-self.problem.constantNumber))
        return costVector
