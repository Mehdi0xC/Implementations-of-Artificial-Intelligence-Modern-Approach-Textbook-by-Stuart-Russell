class Node(object):
    def __init__(self,name):
        self.name = name
        self.neighbours = []
        self.color = 0


    def connect(obj0 , obj1):
        obj0.neighbours.append(obj1)
        obj1.neighbours.append(obj0)
