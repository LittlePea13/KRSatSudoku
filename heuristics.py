from nltk.probability import FreqDist, MLEProbDist
import collections, itertools
import random
def DLCS(clauses):
    freq = collections.defaultdict(int)  # 0 by default
    for x in itertools.chain.from_iterable(clauses):
        freq[abs(x)] += 1
    freq_dist = FreqDist(freq)
    prob_dist = MLEProbDist(freq_dist)
    return prob_dist.generate()
def Random_split(clauses):
    return abs(random.choice([x for x in itertools.chain.from_iterable(clauses)]))