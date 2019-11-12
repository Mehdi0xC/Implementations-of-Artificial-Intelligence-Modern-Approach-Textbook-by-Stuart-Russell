from copy import copy as cp

class Problem(object):
    def __init__(self):
        self.initialState = [3,3,0,0,0]
        self.finalStates = [[0,0,3,3,1]]
        self.nextStates = []
        self.nextAction = []
        self.expandedNodes = 0


    def expand(self,currentState):
        self.nextStates.clear()
        self.nextAction.clear()
        if(currentState[4] == 0):
            if(self.checkConstraints([currentState[0]-2,currentState[1],currentState[2]+2,currentState[3]])):
                self.nextStates.append([currentState[0]-2,currentState[1],currentState[2]+2,currentState[3],1])
                self.nextAction.append("bring 2 humans")
                self.expandedNodes = self.expandedNodes + 1
            if(self.checkConstraints([currentState[0],currentState[1]-2,currentState[2],currentState[3]+2])):
                self.nextStates.append([currentState[0],currentState[1]-2,currentState[2],currentState[3]+2,1])
                self.nextAction.append("bring 2 zombies")
                self.expandedNodes = self.expandedNodes + 1
            if(self.checkConstraints([currentState[0]-1,currentState[1]-1,currentState[2]+1,currentState[3]+1])):
                self.nextStates.append([currentState[0]-1,currentState[1]-1,currentState[2]+1,currentState[3]+1,1])
                self.nextAction.append("bring 1 human , 1 zombie")
                self.expandedNodes = self.expandedNodes + 1
            if(self.checkConstraints([currentState[0]-1,currentState[1],currentState[2]+1,currentState[3]])):
                self.nextStates.append([currentState[0]-1,currentState[1],currentState[2]+1,currentState[3],1])
                self.nextAction.append("bring 1 human")
                self.expandedNodes = self.expandedNodes + 1
            if(self.checkConstraints([currentState[0],currentState[1]-1,currentState[2],currentState[3]+1])):
                self.nextStates.append([currentState[0],currentState[1]-1,currentState[2],currentState[3]+1,1])
                self.nextAction.append("bring 1 zombie")
                self.expandedNodes = self.expandedNodes + 1
        elif(currentState[4] == 1):
            if(self.checkConstraints([currentState[0]+2,currentState[1],currentState[2]-2,currentState[3]])):
                self.nextStates.append([currentState[0]+2,currentState[1],currentState[2]-2,currentState[3],0])
                self.nextAction.append("return 2 humans")
                self.expandedNodes = self.expandedNodes + 1
            if(self.checkConstraints([currentState[0],currentState[1]+2,currentState[2],currentState[3]-2])):
                self.nextStates.append([currentState[0],currentState[1]+2,currentState[2],currentState[3]-2,0])
                self.nextAction.append("return 2 zombies")
                self.expandedNodes = self.expandedNodes + 1
            if(self.checkConstraints([currentState[0]+1,currentState[1]+1,currentState[2]-1,currentState[3]-1])):
                self.nextStates.append([currentState[0]+1,currentState[1]+1,currentState[2]-1,currentState[3]-1,0])
                self.nextAction.append("return 1 human , 1 zombie")
                self.expandedNodes = self.expandedNodes + 1
            if(self.checkConstraints([currentState[0]+1,currentState[1],currentState[2]-1,currentState[3]])):
                self.nextStates.append([currentState[0]+1,currentState[1],currentState[2]-1,currentState[3],0])
                self.nextAction.append("return 1 human")
                self.expandedNodes = self.expandedNodes + 1
            if(self.checkConstraints([currentState[0],currentState[1]+1,currentState[2],currentState[3]-1])):
                self.nextStates.append([currentState[0],currentState[1]+1,currentState[2],currentState[3]-1,0])
                self.nextAction.append("return 1 zombie")
                self.expandedNodes = self.expandedNodes + 1

    def checkConstraints(self,state):
        if(state[1] > state[0]) and (state[0] != 0):
            return False
        if(state[3] > state[2]) and (state[2] != 0):
            return False
        for s in state:
            if s not in [0,1,2,3]:
                return False
        return True

    def flipAction(self,action):
        if(action == "bring 1 human"):
            return ("return 1 human")
        elif(action == "return 1 human"):
            return ("bring 1 human")
        elif(action == "bring 2 humans"):
            return ("return 2 humans")
        elif(action == "return 2 humans"):
            return ("bring 2 humans")
        elif(action == "bring 1 zombie"):
            return ("return 1 zombie")
        elif(action == "return 1 zombie"):
            return ("bring 1 zombie")
        elif(action == "bring 2 zombies"):
            return ("return 2 zombies")
        elif(action == "return 2 zombies"):
            return ("bring 2 zombies")
        elif(action == "bring 1 human , 1 zombie"):
            return ("return 1 human , 1 zombie")
        elif(action == "return 1 human , 1 zombie"):
            return ("bring 1 human , 1 zombie")
