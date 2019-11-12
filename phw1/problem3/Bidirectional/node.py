class Node(object):
    def __init__(self,state,parent,action):
        self.state = state
        self.parent = parent
        self.action = action
        self.children = []

    def addChild(self,obj):
        self.children.append(obj)

            
