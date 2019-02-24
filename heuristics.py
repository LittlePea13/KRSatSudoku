from nltk.probability import FreqDist, MLEProbDist
import collections, itertools
from simplificator import sign
import random
import numpy as np
from collections import Counter

def DLCS_mod(clauses):
    'Not really DLCS, it creates a frequency dict and samples from it'
    freq = Counter([abs(x) for x in itertools.chain.from_iterable(clauses)])
    freq_dist = FreqDist(freq)
    prob_dist = MLEProbDist(freq_dist)
    return prob_dist.generate()

def DLCS(clauses):
    data_neq = Counter([x for x in itertools.chain.from_iterable(clauses)])
    data = Counter([abs(x) for x in itertools.chain.from_iterable(clauses)])
    split = data.most_common(1)[0][0]
    print(split*(-1, 1)[data_neq[split] > data[split]/2])
    return split*(-1, 1)[data_neq[split] > data[split]/2]

def Random_split(clauses):
    return abs(random.choice([x for x in itertools.chain.from_iterable(clauses)]))

def Jeroslow_wang(clauses):
    jeroslow_values = {}
    for clause in clauses:
        for literal in clause:
            if sign(literal) == 1:
                if literal in jeroslow_values:
                    jeroslow_values[literal] += pow(2,-len(clause))
                else:
                    jeroslow_values[literal] = pow(2,-len(clause))

    return max(jeroslow_values, key=jeroslow_values.get)

def Row_wise(clauses):
    return sorted(set([abs(x) for x in itertools.chain.from_iterable(clauses)]), key=lambda x: str(x)[0])[0]
def Column_wise(clauses):
    return sorted(set([abs(x) for x in itertools.chain.from_iterable(clauses)]), key=lambda x: str(x)[1])[0]
def Block_wise(clauses):
    return sorted(set([abs(x) for x in itertools.chain.from_iterable(clauses)]), key=lambda x: str(np.ceil(int(str(x)[0])/3)) + str(np.ceil(int(str(x)[1])/3)))[0]