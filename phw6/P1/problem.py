from node import Node
import random as rnd
import numpy as np
import copy as cp

class Problem(object):
    def __init__(self,colors):
        nodes = []
        self.population = 12
        self.colors = colors
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

    def getCost(self, graph):
        cost = 0
        for node0 in graph:
            for node1 in graph:
                if((node1 in node0.neighbours) and node0.color == node1.color):
                    cost = cost + 1
        return cost

    def nextStatesGenerator(self,graph):
        nextStates = []

        for nodeNum in range(len(graph)):
            for i in range(self.colors):
                newGraph = cp.deepcopy(graph)
                newGraph[nodeNum].color = i
                nextStates.append(newGraph)
        return nextStates

    def makeRandomState(self,graph):
        newGraph = cp.deepcopy(graph)
        for node in newGraph:
            node.color = np.random.randint(0,self.colors)
        return newGraph


    def nextStateGenerator(self,graph):
        newGraph = cp.deepcopy(graph)
        randomNode = np.random.randint(0,len(graph))
        randomColor = np.random.randint(0,self.colors)
        newGraph[randomNode].color = randomColor
        return newGraph


    def printX(self,graph):
        for node in graph:
            print(str(node.name) + " : " + str(node.color))
