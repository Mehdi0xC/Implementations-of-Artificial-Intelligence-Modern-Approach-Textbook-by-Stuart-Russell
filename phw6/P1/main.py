from problem import Problem
from algorithm import algorithm


p = Problem(colors=4)
s = algorithm(p)
# s.stochasticHillClimbingSearch(runningTime=10)
# s.firstBestHillClimbingSearch(runningTime=10)
s.randomRestartHillClimbingSearch(runningTime=10)
