class Node(object):
    def __init__(self,data,parent,action,costFromStart,costToGoal):
        self.data = data
        self.parent = parent
        self.action = action
        self.costFromStart = costFromStart
        self.costToGoal = costToGoal
        self.children = []

    def append(self,obj):
        self.children.append(obj)
