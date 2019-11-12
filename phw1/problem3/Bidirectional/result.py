class Result(object):
    def __init__(self, status):
        self.status = status
        self.path = []

    def changeStatus(self,status):
        self.status = status

    def addToPath(self,path):
        self.path.append(path)
