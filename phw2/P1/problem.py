import random as rnd
import numpy as np
import copy as cp

class Problem(object):
    def __init__(self,queensNumber):
        self.map = []
        self.n = queensNumber
        for i in range(0,self.n):
            vector = []
            for j in range(0,self.n):
                vector.append(0)
            self.map.append(vector)    
        self.heuristic = 0

    def makeState(self):
        newMap = cp.deepcopy(self.map)
        for i in range(0,self.n):
            newMap[i][int(np.ceil(rnd.random()*(self.n-1)))] = 1
        return newMap

    def printX(self,inputMap):
        for i in range(0,self.n):
            print(inputMap[i][:])
        print()

    def findThreats(self , i , j , inputMap):
        threats = 0;
        row = i;
        column = j;
        for k in range(0,self.n):
            if(inputMap[i][k] == 1):
                threats = threats + 1
        for k in range(0,self.n):
            if(inputMap[k][j] == 1):
                threats = threats + 1
        while(i<self.n and j<self.n):
            if(inputMap[i][j] == 1):
                threats = threats + 1
            i = i + 1
            j = j + 1
        i = row
        j = column
        while(i>-1 and j>-1):
            if(inputMap[i][j] == 1):
                threats = threats + 1
            i = i - 1
            j = j - 1
        i = row
        j = column
        while(i>-1 and j<self.n):
            if(inputMap[i][j] == 1):
                threats = threats + 1
            i = i - 1
            j = j + 1
        i = row
        j = column
        while(i<self.n and j>-1):
            if(inputMap[i][j] == 1):
                threats = threats + 1
            i = i + 1
            j = j - 1
        return (threats-6);

    def getCost(self , inputMap):
        heuristic = 0;
        for i in range(0,self.n):
            for j in range(0,self.n):
                if inputMap[i][j] == 1:
                    heuristic = heuristic + self.findThreats(i , j , inputMap)
        return heuristic

    def nextStatesGenerator(self,inputMap):
        maps = []
        for i in range(0,self.n):
            for j in range(0,self.n):
                if (inputMap[i][j] == 1):
                    if(j-1>=0):
                        imagedMap = cp.deepcopy(inputMap)
                        imagedMap[i][j] = 0
                        imagedMap[i][j-1] = 1
                        maps.append(imagedMap)
                    if(j+1<self.n):
                        imagedMap = cp.deepcopy(inputMap)
                        imagedMap[i][j] = 0
                        imagedMap[i][j+1] = 1
                        maps.append(imagedMap)
        return maps
