from problem import Problem
from algorithm import Algorithm
p = Problem()
a = Algorithm(p)
x = a.SA(mode=2 , runningTime=10 , simulatedAnnealingTrials=10000)
p.printX(x[0])
print("final cost is (number of missmatches in dictionary) : " + str(x[1]))
