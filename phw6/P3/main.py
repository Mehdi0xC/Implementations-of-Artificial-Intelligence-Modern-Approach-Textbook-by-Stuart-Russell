from problem import Problem
from algorithm import Algorithm

p = Problem(population=10)
a = Algorithm(p,crossOverRate=0.4 , mutationRate=0.1, trials=100)
chromosomes = a.genetics()
for c in chromosomes:
    print(c)
