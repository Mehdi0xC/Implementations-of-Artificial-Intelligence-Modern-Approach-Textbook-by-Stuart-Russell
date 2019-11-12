class Node(object):
    def __init__(self,  data , parent , action , costFromStart , costToGoal):
        self.data = data
        self.parent = parent
        self.children = []
        self.action = action
        self.costFromStart = costFromStart
        self.costToGoal = costToGoal

    def append(self, obj):
        self.children.append(obj)
