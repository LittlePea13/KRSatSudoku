def parse_rules(filename):
    clauses = []
    for clause in open(filename):
        if clause.startswith('c'):
            continue
        if clause.startswith('p'):
            n_units = clause.split()[2]
            continue
        clause = [int(x) for x in clause[:-2].split()]
        clauses.append(clause)
    return clauses, int(n_units)

def parse_sudoku(filename):
    units = {}
    for clause in open(filename):
        units[clause[:-2]] = clause[-2]
    return units