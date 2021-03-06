sign = lambda x: (1, -1)[x < 0]

def simplification(clauses, variables, sat = True):
    '''
    Returns a modified list of clauses, 
        - Looks for tautologies and deletes the clauses with them
        - Looks for pure literals and adds them to the variables
        - Look for unit clauses, sets them in variables and deletes the clause
    If a contradiction is encountered, it returns the same variables with a false flag
    ''' 
    dict_pure = {}
    checked = set()
    new_clauses = []
    for i, clause in enumerate(clauses):
        seen = set()
        tautology = False
        for x in clause:
            if abs(x) in dict_pure:
                if dict_pure[abs(x)] != sign(x):
                    del dict_pure[abs(x)]
                    checked.add(abs(x))
            elif abs(x) not in checked:
                dict_pure[abs(x)] = sign(x)
            if -x in seen:
                tautology = True
            seen.add(x)
        if len(clause) == 1:
            if abs(clause[0]) in variables and variables[abs(clause[0])] != sign(clause[0]):
                new_clauses = clauses
                sat = False
                break
            else:
                variables[abs(clause[0])]=sign(clause[0])
            continue
        elif tautology:
            continue
        new_clauses.append(clause)
        
    for var, value in dict_pure.items():
        if var in variables and variables[var] != value:
            new_clauses = clauses
            sat = False
            break
        else:
            variables[var]=value 
    return new_clauses, variables, sat

def simplification_sudoku(clauses, variables, sat = True):
    '''
    Returns a modified list of clauses, only for unit literals
        - Look for unit clauses, sets them in variables and deletes the clause
    If a contradiction is encountered, it returns the same variables with a false flag
    ''' 
    checked = set()
    new_clauses = []
    for i, clause in enumerate(clauses):
        seen = set()
        if len(clause) == 1:
            if abs(clause[0]) in variables and variables[abs(clause[0])] != sign(clause[0]):
                new_clauses = clauses
                sat = False
                return clauses, variables, sat
            else:
                variables[abs(clause[0])]=sign(clause[0])
            continue
        new_clauses.append(clause)
    return new_clauses, variables, sat

def update_clauses(clauses, var_dict):
    '''
    Returns a modified list of clauses, 
        - a clause is not included, if it already has a true literal
        - a modified clause is included, otherwise
            - modification of clause, if a literal has been set false already
            - no change, othwerwise
    '''
    new_clauses = []
    for clause in clauses:
        new_clause = []
        for literal in clause:
            if abs(literal) in var_dict:
                sign_of_literal = sign(var_dict[abs(literal)] * literal) 
                if sign_of_literal == 1:
                    #skip clause
                    new_clause = None
                    break

                #else: skip literal
            else:
                new_clause.append(literal)

        if new_clause != None:
            new_clauses.append(new_clause)
            
    return new_clauses