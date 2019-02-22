import os
import sys
def parse_rules(filename):
    clauses = []
    variables = set()
    for clause in open(filename):
        if clause.startswith('c'):
            continue
        if clause.startswith('p'):
            n_variables = clause.split()[2]
            continue
        clause_el = []
        for x in clause[:-2].split():
            clause_el.append(int(x))
            variables.add(abs(int(x)))
        clauses.append(clause_el)
    return clauses, len(variables), variables

#we can take the literals while we parse the problem.

def parse_sudoku(filename):
    units = {}
    for clause in open(filename):
        units[clause[:-2]] = clause[-2]
    return units

if __name__ == '__main__':
    filename = sys.argv[1]
    parse_rules(filename)