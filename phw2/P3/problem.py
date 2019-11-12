import random as rnd
import numpy as np
import copy as cp

class Problem(object):
    def __init__(self , population , equationTerms , constantNumber ,factors):
        self.chromosomes = []
        self.population = population
        self.equationTerms = equationTerms
        self.constantNumber = constantNumber
        self.factors = factors
