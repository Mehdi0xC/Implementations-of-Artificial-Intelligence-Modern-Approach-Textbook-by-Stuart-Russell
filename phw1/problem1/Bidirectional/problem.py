class Problem(object):
    def __init__(self):
        self.initialState = [0,0]
        self.finalStates = [[0,2] , [1,2] , [2,2] , [3,2]]
        self.nextStates = []
        self.nextAction = []

    def expand(self,currentState):
        self.nextStates.clear()
        self.nextAction.clear()
        if(currentState[0] < 3):
            self.nextStates.append([3,currentState[1]])
            self.nextAction.append("Fill 3L Jug")
        if(currentState[1] < 4):
            self.nextStates.append([currentState[0],4])
            self.nextAction.append("Fill 4L Jug")
        if(currentState[0] > 0):
            self.nextStates.append([0,currentState[1]])
            self.nextAction.append("Empty 3L Jug")
        if(currentState[1] > 0):
            self.nextStates.append([currentState[0],0])
            self.nextAction.append("Empty 4L Jug")
        if(((currentState[0] + currentState[1]) <=  4) and (currentState[0] > 0)):
            self.nextStates.append([0,currentState[0] + currentState[1]])
            self.nextAction.append("Pour 3L into 4L Jug")
        elif(((currentState[0] + currentState[1]) >  4) and (currentState[0] > 0)):
            self.nextStates.append([currentState[0] - (4 - currentState[1]),4])
            self.nextAction.append("Pour 3L into 4L Jug")
        if(((currentState[0] + currentState[1]) <=  3) and (currentState[1] > 0)):
            self.nextStates.append([currentState[0]+currentState[1],0])
            self.nextAction.append("Pour 4L into 3L Jug")
        elif(((currentState[0] + currentState[1]) >  3) and (currentState[1] > 0)):
            self.nextStates.append([3,currentState[1] - (3 - currentState[0])])
            self.nextAction.append("Pour 4L into 3L Jug")

    def flipAction(self,action):
        if(action == "Fill 3L Jug"):
            return ("Empty 3L Jug")
        if(action == "Fill 4L Jug"):
            return ("Empty 4L Jug")
        if(action == "Empty 3L Jug"):
            return ("Fill 3L Jug")
        if(action == "Empty 4L Jug"):
            return ("Fill 4L Jug")
        if(action == "Pour 3L into 4L Jug"):
            return ("Pour 4L into 3L Jug")
        if(action == "Pour 4L into 3L Jug"):
            return ("Pour 3L into 4L Jug")
