from heuristics import Random_split
from simplificator import update_clauses, simplification, simplification_sudoku, sign
from statistics import StatCollector
from sanity import print_sudoku, check_sudoku
from parser import parse_rules
from statistics import StatCollector
import time

def dp(clauses, variables, heuristics_func = Random_split, stat_collector=None):
    '''
        Recursive Solver
    '''
    
    if clauses == []:
        return True, variables
    for clause in clauses:
        if clause == []:
            #INC backtrack
            if stat_collector != None:
                stat_collector.backtrack()
            return False, variables
        
    new_clauses, variables, sat = simplification(clauses, variables)
    new_clauses = update_clauses(new_clauses, variables)
    
    if stat_collector != None:
        stat_collector.create_timestamp(variables)

    if len([1 for element in clauses if len(element)==1])>1:
        return dp(new_clauses, variables, heuristics_func, stat_collector)
    
    split = heuristics_func(new_clauses)
    #INC split
    if stat_collector != None:
        stat_collector.split(abs(split))
    
    sat, variables_split = dp(update_clauses(new_clauses, {**variables,**{abs(split):sign(split)}}), {**variables,**{abs(split):sign(split)}}, heuristics_func, stat_collector)
    if sat is False:
        sat, variables_split = dp(update_clauses(new_clauses, {**variables,**{abs(split):-sign(split)}}), {**variables,**{abs(split):-sign(split)}}, heuristics_func, stat_collector)
    
    return sat, variables_split

def davis_putnam(filename, heuristics, print_results = False):
    rules,_,_ = parse_rules('sudoku-rules.txt')
    sudoku_clauses,_,_ = parse_rules(filename)
    clauses = sudoku_clauses + rules
    t0 = time.time()
    stat_collector = StatCollector()
    result, variables = dp(clauses, {},  heuristics, stat_collector)
    t1 = time.time()
    if print_results:
        print('Time to solve sudoku:', t1-t0)
        print('Result ', result)
        print_sudoku(sorted([k for k,v in variables.items() if v>0]))
    stat_collector.print_stats(printing=print_results)
    
    
    return result, t1-t0, stat_collector
