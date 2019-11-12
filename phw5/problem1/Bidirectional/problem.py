class Problem(object):
    def __init__(self):
        # we define the problem so that there are [3X humans , 3X zombies] on the starting position
        # and [0X humans , 0X zombies on other side of river]
        self.initialState = [0,0]
        self.map = [4,4]
        self.wallCount = 4
        self.walls = [[2,1,3,1],[2,2,3,2],[1,2,1,3],[2,2,2,3]]
        self.finalStates = [[4,4]]
        self.nextStates = []
        self.nextAction = []
        self.expandedNodes = 0


    def expand(self,currentState):
        self.nextStates.clear()
        self.nextAction.clear()
        if(currentState[0] < self.map[0]):
            if(not(self.isWall(currentState,[currentState[0]+1,currentState[1]]))):
                self.nextStates.append([currentState[0]+1,currentState[1]])
                self.nextAction.append("r")
                self.expandedNodes = self.expandedNodes+1
        if(currentState[1] < self.map[1]):
            if(not(self.isWall(currentState,[currentState[0],currentState[1]+1]))):
                self.nextStates.append([currentState[0],currentState[1]+1])
                self.nextAction.append("d")
                self.expandedNodes = self.expandedNodes+1
        if(currentState[0] > 0):
            if(not(self.isWall(currentState,[currentState[0]-1,currentState[1]]))):
                self.nextStates.append([currentState[0]-1,currentState[1]])
                self.nextAction.append("l")
                self.expandedNodes = self.expandedNodes+1
        if(currentState[1] > 0):
            if(not(self.isWall(currentState,[currentState[0],currentState[1]-1]))):
                self.nextStates.append([currentState[0],currentState[1]-1])
                self.nextAction.append("u")
                self.expandedNodes = self.expandedNodes+1

    def isWall(self,pos1,pos2):
        for i in range(self.wallCount):
            if(pos1 == self.walls[i][0:2] and pos2 == self.walls[i][2:4]):
                return True
            elif(pos2 == self.walls[i][0:2] and pos1 == self.walls[i][2:4]):
                return True
        return False

    def flipAction(self,action):
        if(action == "l"):
            return "r"
        if(action == "r"):
            return "l"
        if(action == "u"):
            return "d"
        if(action == "d"):
            return "u"
