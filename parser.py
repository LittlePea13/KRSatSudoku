def parse_rules(filename):
    clauses = []
    units = set()
    for clause in open(filename):
        if clause.startswith('c'):
            continue
        if clause.startswith('p'):
            n_units = clause.split()[2]
            continue
        clause_el = []
        for x in clause[:-2].split():
            clause_el.append(int(x))
            units.add(abs(int(x)))
        clauses.append(clause_el)
    return clauses, len(units), units

#we can take the literals while we parse the problem.

def parse_sudoku(filename):
    units = {}
    for clause in open(filename):
        units[clause[:-2]] = clause[-2]
    return units
