import collections, itertools
from simplificator import sign
import random
import math
from collections import Counter

def DLCS(clauses):
    data_neq = Counter([x for x in itertools.chain.from_iterable(clauses)])
    data = Counter([abs(x) for x in itertools.chain.from_iterable(clauses)])
    split = data.most_common(1)[0][0]
    return split*(-1, 1)[data_neq[split] > data[split]/2]

def Random_split(clauses):
    return random.choice([x for x in itertools.chain.from_iterable(clauses)])

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
    return sorted(set([abs(x) for x in itertools.chain.from_iterable(clauses)]), key=lambda x: get_row(x))[0]
def Column_wise(clauses):
    return sorted(set([abs(x) for x in itertools.chain.from_iterable(clauses)]), key=lambda x: get_column(x))[0]
def Block_wise(clauses):
    return sorted(set([abs(x) for x in itertools.chain.from_iterable(clauses)]), key=lambda x: get_block(x))[0]

def get_row(variable):
    return str(variable)[0]
def get_column(variable):
    return str(variable)[1]
def get_block(variable):
    return (int(math.ceil(int(str(variable)[0])/3))-1)*3 + int(math.ceil(int(str(variable)[1])/3))

def Row_wise_rand(clauses):
    clauses_by_row = [[],[],[],[],[],[],[],[],[]]
    for element in [x for x in itertools.chain.from_iterable(clauses)]:
        clauses_by_row[int(get_row(abs(element)))-1].append(element)
    for element in clauses_by_row:
        if len(element)>0:
             return random.choice(element)
def Column_wise_rand(clauses):
    clauses_by_column = [[],[],[],[],[],[],[],[],[]]
    for element in [x for x in itertools.chain.from_iterable(clauses)]:
        clauses_by_column[int(get_column(abs(element)))-1].append(element)
    for element in clauses_by_column:
        if len(element)>0:
             return random.choice(element)

def Block_wise_rand(clauses):
    clauses_by_block = [[],[],[],[],[],[],[],[],[]]
    for element in [x for x in itertools.chain.from_iterable(clauses)]:
        clauses_by_block[int(get_block(abs(element)))-1].append(element)
    for element in clauses_by_block:
        if len(element)>0:
             return random.choice(element)

def Row_wise_lenght(clauses):
    clauses_by_row = [[],[],[],[],[],[],[],[],[]]
    for element in [x for x in itertools.chain.from_iterable(clauses)]:
        clauses_by_row[int(get_row(abs(element)))-1].append(element)
    for element in sorted(clauses_by_row, key= lambda x: len(x)):
        if len(element)>0:
             return random.choice(element)

def Row_wise_lenght_set(clauses):
    clauses_by_row = [[],[],[],[],[],[],[],[],[]]
    for element in [x for x in itertools.chain.from_iterable(clauses)]:
        clauses_by_row[int(get_row(abs(element)))-1].append(element)
    for element in sorted(clauses_by_row, key= lambda x: len(set(x))):
        if len(element)>0:
             return random.choice(set(element))

def Column_wise_lenght(clauses):
    clauses_by_column = [[],[],[],[],[],[],[],[],[]]
    for element in [x for x in itertools.chain.from_iterable(clauses)]:
        clauses_by_column[int(get_column(abs(element)))-1].append(element)
    for element in sorted(clauses_by_column, key= lambda x: len(x)):
        if len(element)>0:
             return random.choice(element)

def Block_wise_lenght(clauses):
    clauses_by_block = [[],[],[],[],[],[],[],[],[]]
    for element in [x for x in itertools.chain.from_iterable(clauses)]:
        clauses_by_block[int(get_block(abs(element)))-1].append(element)
    for element in sorted(clauses_by_block, key= lambda x: len(x)):
        if len(element)>0:
             return random.choice(element)