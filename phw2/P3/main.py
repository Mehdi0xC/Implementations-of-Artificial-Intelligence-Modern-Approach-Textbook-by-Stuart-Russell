from problem import Problem
from algorithm import Algorithm
p = Problem(population=100,equationTerms=4,constantNumber=40,factors=[1,2,3,4])
a = Algorithm(p)
chromosomes = a.genetics(crossOverRate=0.4 , mutationRate=0.01, trials=1000)
for c in chromosomes:
    print(c)
