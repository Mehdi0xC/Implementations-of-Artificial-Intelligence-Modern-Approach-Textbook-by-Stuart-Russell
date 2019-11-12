from copy import copy as cp
import random as rnd
class Problem(object):
    def __init__(self):
        self.initialState = ['y','b','y','b','g','y','g','y','w','g','w','g','b','w','b','w','r','r','r','r','o','o','o','o']
        self.finalStates = [['y','y','y','y','g','g','g','g','w','w','w','w','b','b','b','b','r','r','r','r','o','o','o','o']]
        self.nextStates = []
        self.nextAction = []
        self.expandedNodes = 0

    def expand(self,currentState):
        self.nextStates.clear()
        self.nextAction.clear()

        self.nextStates.append([
        currentState[0],currentState[1],currentState[19],currentState[17],
        currentState[6],currentState[4],currentState[7],currentState[5],
        currentState[22],currentState[20],currentState[10],currentState[11],
        currentState[12],currentState[13],currentState[14],currentState[15],
        currentState[16],currentState[8],currentState[18],currentState[9],
        currentState[2],currentState[21],currentState[3],currentState[23]
        ])
        self.nextAction.append("t")
        self.expandedNodes = self.expandedNodes+1

        self.nextStates.append([
        currentState[0],currentState[1],currentState[20],currentState[22],
        currentState[5],currentState[7],currentState[4],currentState[6],
        currentState[17],currentState[19],currentState[10],currentState[11],
        currentState[12],currentState[13],currentState[14],currentState[15],
        currentState[16],currentState[3],currentState[18],currentState[2],
        currentState[9],currentState[21],currentState[8],currentState[23]
        ])
        self.nextAction.append("tc")
        self.expandedNodes = self.expandedNodes+1

        self.nextStates.append([
        currentState[0],currentState[13],currentState[2],currentState[15],
        currentState[4],currentState[1],currentState[6],currentState[3],
        currentState[8],currentState[5],currentState[10],currentState[7],
        currentState[12],currentState[9],currentState[14],currentState[11],
        currentState[16],currentState[17],currentState[18],currentState[19],
        currentState[21],currentState[23],currentState[20],currentState[22]
        ])
        self.nextAction.append("rc")
        self.expandedNodes = self.expandedNodes+1

        self.nextStates.append([
        currentState[2],currentState[0],currentState[3],currentState[1],
        currentState[20],currentState[21],currentState[6],currentState[7],
        currentState[8],currentState[9],currentState[10],currentState[11],
        currentState[12],currentState[13],currentState[17],currentState[16],
        currentState[4],currentState[5],currentState[18],currentState[19],
        currentState[15],currentState[14],currentState[22],currentState[23]
        ])
        self.nextAction.append("f")
        self.expandedNodes = self.expandedNodes+1

        self.nextStates.append([
        currentState[1],currentState[3],currentState[0],currentState[2],
        currentState[16],currentState[17],currentState[6],currentState[7],
        currentState[8],currentState[9],currentState[10],currentState[11],
        currentState[12],currentState[13],currentState[21],currentState[20],
        currentState[15],currentState[14],currentState[18],currentState[19],
        currentState[4],currentState[5],currentState[22],currentState[23]
        ])
        self.nextAction.append("fc")
        self.expandedNodes = self.expandedNodes+1

        self.nextStates.append([
        currentState[0],currentState[5],currentState[2],currentState[7],
        currentState[4],currentState[9],currentState[6],currentState[11],
        currentState[8],currentState[13],currentState[10],currentState[15],
        currentState[12],currentState[1],currentState[14],currentState[3],
        currentState[16],currentState[17],currentState[18],currentState[19],
        currentState[22],currentState[20],currentState[23],currentState[21]
        ])
        self.nextAction.append("r")
        self.expandedNodes = self.expandedNodes+1
