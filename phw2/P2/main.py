from problem import Problem
from algorithm import Algorithm
p = Problem()
a = Algorithm(p)
x = a.SA(mode=0 , runningTime=10 , simulatedAnnealingTrials=10000)
p.printX(x[0] , x[1])
