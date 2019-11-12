from printer import Printer
from copy import copy as cp
import random as rnd
class Problem(object):
    def __init__(self,initialState):
        self.finalStates = [[0,1,2,3,4,5,6,7,8]]
        self.nextStates = []
        self.nextAction = []
        self.initialState = initialState

    def randomInitialStateGenerator(self):
        i = 0
        while(i<9):
            randomNumber = rnd.randrange(0,9)
            if (randomNumber not in self.initialState):
                self.initialState.append(randomNumber)
                i=i+1




    def expand(self,currentState):
        self.nextStates.clear()
        self.nextAction.clear()
        pos = currentState.index(0)
        self.nextState0 = cp(currentState)
        self.nextState1 = cp(currentState)
        self.nextState2 = cp(currentState)
        self.nextState3 = cp(currentState)
        if(pos == 0):
            self.nextState0[0] = currentState[1]
            self.nextState0[1] = 0;
            self.nextStates.append(self.nextState0)
            self.nextAction.append("left")
            self.nextState1[0] = currentState[3]
            self.nextState1[3] = 0;
            self.nextStates.append(self.nextState1)
            self.nextAction.append("up")
        if(pos == 1):
            self.nextState0[1] = currentState[0]
            self.nextState0[0] = 0;
            self.nextStates.append(self.nextState0)
            self.nextAction.append("right")
            self.nextState1[1] = currentState[2]
            self.nextState1[2] = 0;
            self.nextStates.append(self.nextState1)
            self.nextAction.append("left")
            self.nextState2[1] = currentState[4]
            self.nextState2[4] = 0;
            self.nextStates.append(self.nextState2)
            self.nextAction.append("up")
        if(pos == 2):
            self.nextState0[2] = currentState[1]
            self.nextState0[1] = 0;
            self.nextStates.append(self.nextState0)
            self.nextAction.append("right")
            self.nextState1[2] = currentState[5]
            self.nextState1[5] = 0;
            self.nextStates.append(self.nextState1)
            self.nextAction.append("up")
        if(pos == 3):
            self.nextState0[3] = currentState[0]
            self.nextState0[0] = 0;
            self.nextStates.append(self.nextState0)
            self.nextAction.append("down")
            self.nextState1[3] = currentState[4]
            self.nextState1[4] = 0;
            self.nextStates.append(self.nextState1)
            self.nextAction.append("left")
            self.nextState2[3] = currentState[6]
            self.nextState2[6] = 0;
            self.nextStates.append(self.nextState2)
            self.nextAction.append("up")
        if(pos == 4):
            self.nextState0[4] = currentState[1]
            self.nextState0[1] = 0;
            self.nextStates.append(self.nextState0)
            self.nextAction.append("down")
            self.nextState1[4] = currentState[3]
            self.nextState1[3] = 0;
            self.nextStates.append(self.nextState1)
            self.nextAction.append("right")
            self.nextState2[4] = currentState[5]
            self.nextState2[5] = 0;
            self.nextStates.append(self.nextState2)
            self.nextAction.append("left")
            self.nextState3[4] = currentState[7]
            self.nextState3[7] = 0;
            self.nextStates.append(self.nextState3)
            self.nextAction.append("up")
        if(pos == 5):
            self.nextState0[5] = currentState[2]
            self.nextState0[2] = 0;
            self.nextStates.append(self.nextState0)
            self.nextAction.append("down")
            self.nextState1[5] = currentState[4]
            self.nextState1[4] = 0;
            self.nextStates.append(self.nextState1)
            self.nextAction.append("right")
            self.nextState2[4] = currentState[8]
            self.nextState2[8] = 0;
            self.nextStates.append(self.nextState2)
            self.nextAction.append("up")
        if(pos == 6):
            self.nextState0[6] = currentState[3]
            self.nextState0[3] = 0;
            self.nextStates.append(self.nextState0)
            self.nextAction.append("down")
            self.nextState1[6] = currentState[7]
            self.nextState1[7] = 0;
            self.nextStates.append(self.nextState1)
            self.nextAction.append("left")
        if(pos == 7):
            self.nextState0[7] = currentState[6]
            self.nextState0[6] = 0;
            self.nextStates.append(self.nextState0)
            self.nextAction.append("right")
            self.nextState1[7] = currentState[4]
            self.nextState1[4] = 0;
            self.nextStates.append(self.nextState1)
            self.nextAction.append("down")
            self.nextState2[7] = currentState[8]
            self.nextState2[8] = 0;
            self.nextStates.append(self.nextState2)
            self.nextAction.append("left")
        if(pos == 8):
            self.nextState0[8] = currentState[5]
            self.nextState0[5] = 0;
            self.nextStates.append(self.nextState0)
            self.nextAction.append("down")
            self.nextState1[8] = currentState[7]
            self.nextState1[7] = 0;
            self.nextStates.append(self.nextState1)
            self.nextAction.append("right")
