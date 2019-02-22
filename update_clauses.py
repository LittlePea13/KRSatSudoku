def update_clauses(clauses, var_dict):
	'''
	Returns a modified list of clauses, 
	    - a clause is not included, if it already has a true literal
	    - a modified clause is included, otherwise
		- modification of clause, if a literal has been set false already
		- no change, othwerwise
	'''
# TODO delete old list?
    for clause in clauses:
        new_clause = []
        for literal in clause:
            if abs(literal) in var_dict:
                sign_of_literal = sign(var_dict[abs(literal)] * literal) 
                if sign_of_literal == 1:
                    #skip clause
                    new_clause = []
                    break

                #else: skip literal
            else:
                new_clause.append(literal)

        if new_clause != []:
            new_clauses.append(new_clause)
            
    return new_clauses
