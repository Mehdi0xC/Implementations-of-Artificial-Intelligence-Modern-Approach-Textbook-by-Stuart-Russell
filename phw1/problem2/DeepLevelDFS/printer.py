class Printer(object):
    def __init__(self):
        self.list = []

    def printX(self,list):
        self.list=list
        for i in range (3):
            print('-------' )
            print('|' , end='')
            for j in range (3):
                print(self.list[3*i+j] , end='|')
            print('')
        print('-------' )
