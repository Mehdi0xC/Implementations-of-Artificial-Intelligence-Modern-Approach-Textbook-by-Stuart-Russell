import random as rnd
import numpy as np
import copy as cp

class Problem(object):
    def __init__(self , population):
        self.population = population
        self.genes = [
        'a',
        'b',
        'c',
        'd',
        'e',
        'f',
        'g',
        'h',
        'i',
        'j',
        'k',
        'l',
        'm',
        'n',
        'o',
        'p',
        'q',
        'r',
        's',
        't',
        'u',
        'v',
        'w',
        'x',
        'y',
        'z'
        ]

        self.genCount = len(self.genes)
        self.fitnessFactor0 = ['e','t','a','i','n','o','s','h','r']
        self.fitnessFactor1 = ['th','er','on','an','re','he','in','ed']

    def makeFirstChromosomes(self):
        chromosomes = []
        chromosome = []
        for i in range(0,self.population):
            clone = cp.deepcopy(self.genes)
            while(len(clone)>1):
                chromosome.append(clone.pop(np.random.randint(0,len(clone)-1)))
            chromosome.append(clone[0])
            chromosomes.append(chromosome)
        return chromosomes

    def getCost(self,chromosome):
        leftHalf = chromosome[0:int(self.genCount/2)]
        rightHalf = chromosome[int(self.genCount/2):self.genCount]
        rightLetters = 0
        leftLetters = 0
        rightComb = 0
        leftComb = 0
        for letter in self.fitnessFactor0:
            if letter in rightHalf:
                rightLetters = rightLetters + 1
            elif letter in leftHalf:
                leftLetters = leftLetters + 1
        for comb in self.fitnessFactor1:
            if (self.combInHalf(comb,rightHalf)):
                rightComb = rightComb + 1
            elif (self.combInHalf(comb,leftHalf)):
                leftComb = leftComb + 1
        return (abs(leftComb - rightComb) + abs(leftLetters + rightLetters))

    def combInHalf(self,comb,keyboardHalf):
        level0 = (keyboardHalf[0] + keyboardHalf[1] + keyboardHalf[2] + keyboardHalf[3] + keyboardHalf[4])
        level1 = (keyboardHalf[5] + keyboardHalf[6] + keyboardHalf[7] + keyboardHalf[8])
        level2 = (keyboardHalf[9] + keyboardHalf[10] + keyboardHalf[11] + keyboardHalf[12])
        if comb in level0:
            return True
        elif comb in level1:
            return True
        elif comb in level2:
            return True
        return False


    def combine(self,chromosome0 , chromosome1):
        child = cp.deepcopy(self.genes)
        for gene in self.genes:
            p = np.random.rand()
            print(chromosome0)
            print(chromosome1)
            print(self.getCost(chromosome0))

            if(p<0.5):
                if gene in chromosome0:
                    child[chromosome0.index(gene)] = gene
            else:
                if gene in chromosome1:
                    child[chromosome1.index(gene)] = gene
        return child


    def mutate(self,chromosome):
        rand0 = np.random.randint(0,self.genCount)
        rand1 = np.random.randint(0,self.genCount)
        newChromosome = cp.deepcopy(chromosome)
        newChromosome[rand1] = chromosome[rand0]
        newChromosome[rand0] = chromosome[rand1]
        return newChromosome
