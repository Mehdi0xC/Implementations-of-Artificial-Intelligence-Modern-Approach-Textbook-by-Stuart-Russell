class Result(object):
    def __init__(self, status):
        self.status = status
        self.path = []
        self.bestCost = 0
        self.expandedNodes = 0

    def changeStatus(self,status):
        self.status = status

    def addToPath(self,path):
        self.path.append(path)
