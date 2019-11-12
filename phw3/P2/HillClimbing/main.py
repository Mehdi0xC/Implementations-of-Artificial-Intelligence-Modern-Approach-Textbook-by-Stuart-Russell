from problem import Problem
from algorithm import algorithm


p = Problem(queensNumber=8)
s = algorithm(p)
s.randomRestartHillClimbingSearch(runningTime=10,maxRestarts=10)
