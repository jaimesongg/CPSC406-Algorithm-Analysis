# SAT solver
# Modify and extend as needed

def solve_sat(clauses, assignment):
    # simplifies the CNF formula by applying the current assignment
    def simplify(clauses, assignment):
        simplified = []
        for clause in clauses:
            new_clause = []
            satisfied = False
            for literal in clause:
                var = abs(literal)
                val = assignment.get(var, None)
                if val is not None:
                    # if the literal is satisfied by the assignment, the clause is satisfied
                    if (literal > 0 and val) or (literal < 0 and not val):
                        satisfied = True
                        break # skip clause, its satisfied
                    else:
                        continue
                else:
                    new_clause.append(literal)
            if not satisfied:
                if not new_clause:
                    return None  # clause is unsatisfiable
                simplified.append(new_clause)
        return simplified

# applies unit clause propagation to deduce forced assignments
    def unit_propagate(clauses, assignment):
        changed = True
        while changed:
            changed = False
            # find all unit clauses (single literal)
            unit_clauses = [c[0] for c in clauses if len(c) == 1]
            for literal in unit_clauses:
                var = abs(literal)
                value = literal > 0
                if var in assignment:
                    # conflict: already assigned a different value
                    if assignment[var] != value:
                        return None
                else:
                    # add the forced assignment
                    assignment[var] = value
                    changed = True
                # simplify the formula with the new assignment
                clauses = simplify(clauses, assignment)
                if clauses is None:
                    return None
        return clauses

    # initial simplification with the current assignment
    clauses = simplify(clauses, assignment)
    if clauses is None:
        return None # conflict detected
    if not clauses:
        return assignment # all clauses satisfied

    clauses = unit_propagate(clauses, assignment)
    if clauses is None:
        return None
    if not clauses:
        return assignment

    # choose the first literal of the first clause to branch on
    for clause in clauses:
        for literal in clause:
            var = abs(literal)
            if var not in assignment:
                for value in [True, False]:
                    new_assignment = assignment.copy()
                    new_assignment[var] = value
                    result = solve_sat(clauses, new_assignment)
                    if result is not None:
                        return result # found satisfying assignment
                return None # neither true nor false worked so backtrack
    return None

# example test cases:
if __name__ == "__main__":
    tests = [
        ([[1, 2], [-1], [-2], [-1, -2]], {}, None),
        ([[1, 2], [-1], [2]], {}, {1: False, 2: True}),
        ([[1], [2], [3], [-4], [-5], [-6]], {}, {1: True, 2: True, 3: True, 4: False, 5: False, 6: False}),
        ([[1, -2], [-1, 2], [3], [-3, 4], [-4]], {}, None)
    ]

    for i, (clauses, assignment, expected) in enumerate(tests):
        result = solve_sat(clauses, assignment.copy())
        print(f"Test {i+1}: {'Passed' if result == expected else 'Failed'}")
        print("Result:", result)
        print("Expected:", expected)
        print()
