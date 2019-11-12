from node import Node
import random as rnd
import numpy as np
import copy as cp

class Problem(object):
    def __init__(self):
        nodes = []
        self.population = 12
        for i in range(0,self.population) :
            x = Node(str(i))
            nodes.append(x)
        Node.connect(nodes[0] , nodes[1])
        Node.connect(nodes[0] , nodes[2])
        Node.connect(nodes[1] , nodes[2])
        Node.connect(nodes[1] , nodes[3])
        Node.connect(nodes[1] , nodes[5])
        Node.connect(nodes[2] , nodes[4])
        Node.connect(nodes[3] , nodes[4])
        Node.connect(nodes[3] , nodes[8])
        Node.connect(nodes[4] , nodes[7])
        Node.connect(nodes[5] , nodes[6])
        Node.connect(nodes[6] , nodes[8])
        Node.connect(nodes[6] , nodes[9])
        Node.connect(nodes[6] , nodes[11])
        Node.connect(nodes[7] , nodes[8])
        Node.connect(nodes[8] , nodes[10])
        Node.connect(nodes[9] , nodes[11])
        Node.connect(nodes[10] , nodes[11])
        self.state = nodes
        self.heuristic = 0

    def getCost(self , graph0 , graph1):
        distance = abs(len(graph0) - len(graph1)) + self.countConnections(graph0,graph1)
        return distance

    def countConnections(self , graph0 , graph1):
        connections = 0
        for node in graph0:
            for n in node.neighbours:
                if (n in graph1):
                    connections = connections + 1
        return connections

    def printX(self,subGraph0,subGraph1):
        print('Graph1 Nodes :')
        for i in subGraph0:
            print(i.name)
        print('Graph2 Nodes :')
        for i in subGraph1:
            print(i.name)


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
