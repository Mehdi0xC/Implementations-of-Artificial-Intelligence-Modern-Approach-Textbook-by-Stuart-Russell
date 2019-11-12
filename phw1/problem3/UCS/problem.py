class Problem0(object):
    def __init__(self , rows , columns , field):
        self.initialState = [0,0] #assume that first element is 3L jug and second is 4L
        self.finalStates = [[rows-1 , columns-1]]
        self.nextStates = []
        self.nextAction = []
        self.rows = rows
        self.columns = columns
        self.field = field

    def expand(self,currentState):
        self.nextStates.clear()
        self.nextAction.clear()
        if((currentState[0] < self.rows-1) and (self.field[currentState[0]+1][currentState[1]] != 0)):
            self.nextStates.append([currentState[0]+1 , currentState[1]])
            self.nextAction.append("Move Up")
        if((currentState[0] > 0) and (self.field[currentState[0]-1][currentState[1]] != 0)):
            self.nextStates.append([currentState[0]-1 , currentState[1]])
            self.nextAction.append("Move Down")
        if((currentState[1] < self.columns-1) and (self.field[currentState[0]][currentState[1]+1] != 0)):
            self.nextStates.append([currentState[0] , currentState[1]+1])
            self.nextAction.append("Move Right")
        if((currentState[1] > 0 ) and (self.field[currentState[0]][currentState[1]-1] != 0)):
            self.nextStates.append([currentState[0] , currentState[1]-1])
            self.nextAction.append("Move Left")
     
