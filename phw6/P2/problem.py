from node import Node
import random as rnd
import numpy as np
import copy as cp

class Problem(object):
    def __init__(self):
        table = [
        ['a','p','t'],
        ['m','l','b'],
        ['k','l','o'],
        ['u','o','c']
        ]
        self.dict = ['cool','cat','talk','go']
        self.state = table

    def getCost(self , table):
        maxCost = 1000*len(self.dict);
        for word in self.dict:
            maxCost = maxCost + len(word)
        correctLetters = 0
        for word in self.dict:
            correctLetters = correctLetters + self.validator(table,word)[0]
            correctWords = self.validator(table,word)[0]
        cost =  maxCost - correctLetters - 1000*correctWords
        return cost


    def validator(self , table , word):
        matches = 0
        wordMatches = 0
        wordCheckingMatches = 0

        for r in range(len(table)):
            for c in range(len(table[0])):
                if (word[0] == table[r][c]):
                    matches = matches+1
                    wordCheckingMatches = wordCheckingMatches+1
                    for i in range(1,len(word)):
                        checkNeighbourhood = self.isNeighbour(table,r,c,word[i])
                        if(checkNeighbourhood[0] == True):
                            r=checkNeighbourhood[1]
                            c=checkNeighbourhood[2]
                            matches = matches+1
                            wordCheckingMatches = wordCheckingMatches+1
                            if(wordCheckingMatches == len(word)):
                                wordMatches = wordMatches+1
                wordCheckingMatches = 0
        return [matches,wordMatches]

    def isNeighbour(self , table , r , c , letter):
        if(r>0):
            if(table[r-1][c] == letter):
                return [True,r,c]
        if(c>0):
            if(table[r][c-1] == letter):
                return [True,r,c]
        if(r<len(table)-1):
            if(table[r+1][c] == letter):
                return [True,r,c]
        if(c<len(table[0])-1):
            if(table[r][c+1] == letter):
                return [True,r,c]
        return [False,0,0]

    def printX(self,table):
        for r in range(len(table)):
            for c in range(len(table[0])):
                print(table[r][c] + " ")
            print("")


    def nextStateGenerator(self,table):
        newTable = cp.deepcopy(table)
        randrow0 = np.random.randint(0,len(table))
        randrow1 = np.random.randint(0,len(table))
        randCol0 = np.random.randint(0,len(table[0]))
        randCol1 = np.random.randint(0,len(table[0]))
        newTable[randrow0][randCol0] = table[randrow1][randCol1]
        newTable[randrow1][randCol1] = table[randrow0][randCol0]
        return newTable
