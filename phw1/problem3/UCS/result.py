class Result(object):
    def __init__(self,  status ):
        self.status = status
        self.path = []

    def addToPath(self, obj):
        self.path.append(obj)

    def changeStatus(self, status ):
        self.status = status
