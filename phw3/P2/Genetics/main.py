from problem import Problem
from algorithm import Algorithm

p = Problem(queensNumber=8,population=20)
a = Algorithm(p,crossOverRate=0.4 , mutationRate=0.4, trials=100 , childrenCount=50)
chromosomes = a.genetics()
print("final chromosomes are :")
for c in chromosomes:
    p.printX(c)
