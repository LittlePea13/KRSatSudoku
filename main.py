import random
from simplificator import update_clauses, simplification, simplification_sudoku, sign
from heuristics import Random_split, DLCS
from sanity import print_sudoku, check_sudoku
from parser import parse_rules
import time
import sys

def DL(clauses, variables, n_iterations, heuristics = Random_split):
    '''
        Recursive Solver
    '''
    if clauses == []:
        return True, variables
    for clause in clauses:
        if clause == []:
            return False, variables
    new_clauses, variables, sat = simplification(clauses, variables)
    new_clauses = update_clauses(new_clauses, variables)
    if len([1 for element in clauses if len(element)==1])>1:
        return DL(new_clauses, variables, n_iterations, heuristics)
    split = heuristics(new_clauses)
    value = 1 if random.random() < 0.5 else -1
    sat, variables_split = DL(update_clauses(new_clauses, {**variables,**{split:value}}), {**variables,**{split:value}}, n_iterations +1, heuristics)
    if sat is False:
        sat, variables_split = DL(update_clauses(new_clauses, {**variables,**{split:-value}}), {**variables,**{split:-value}}, n_iterations +1, heuristics)
    return sat, variables_split

def main(filename, heuristics):
    rules,_,_ = parse_rules('sudoku-rules.txt')
    sudoku_clauses,_,_ = parse_rules(filename)
    clauses = sudoku_clauses + rules
    t0 = time.time()
    result, variables = DL(clauses, {}, 1)
    t1 = time.time()
    print('Time to solve sudoku:', t1-t0)
    print('Result ', result)
    print_sudoku(sorted([k for k,v in variables.items() if v>0]))
    return result

if __name__ == '__main__':
    # Example to run: python main.py sudokus/damnhard.sdk_0.txt 1
    filename = sys.argv[1]
    heur = sys.argv[2]
    if heur == 1 or heur is None:
        heuristics = Random_split
    else:
        heuristics = DLCS
    main(filename, heuristics)