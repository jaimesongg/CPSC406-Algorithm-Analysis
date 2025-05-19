import sat_solver

# Sudoku solver using SAT solver
# Modify and extend as needed

# encode (row, col, digit) into a unique variable 1..729
def varnum(r, c, d):
    return 81 * (r - 1) + 9 * (c - 1) + d

# decode back from variable number to (row, col, digit)
def decode_var(v):
    v -= 1
    d = (v % 9) + 1
    c = ((v // 9) % 9) + 1
    r = (v // 81) + 1
    return r - 1, c - 1, d

def sudoku_encode(grid):
    clauses = []

    # cell constraints: one digit per cell
    for r in range(1, 10):
        for c in range(1, 10):
            clauses.append([varnum(r, c, d) for d in range(1, 10)])  # at least one number
            for d1 in range(1, 10):
                for d2 in range(d1 + 1, 10):
                    # at most one number
                    clauses.append([-varnum(r, c, d1), -varnum(r, c, d2)])

    # row constraints: each digit appears once per row
    for r in range(1, 10):
        for d in range(1, 10):
            clauses.append([varnum(r, c, d) for c in range(1, 10)])
            for c1 in range(1, 10):
                for c2 in range(c1 + 1, 10):
                    clauses.append([-varnum(r, c1, d), -varnum(r, c2, d)])

    # column constraints: each digit appears once per column
    for c in range(1, 10):
        for d in range(1, 10):
            clauses.append([varnum(r, c, d) for r in range(1, 10)])
            for r1 in range(1, 10):
                for r2 in range(r1 + 1, 10):
                    clauses.append([-varnum(r1, c, d), -varnum(r2, c, d)])

    # block constraints: each digit appears once per 3x3 block
    for br in range(0, 3):
        for bc in range(0, 3):
            for d in range(1, 10):
                cells = [varnum(r, c, d)
                         for r in range(1 + br * 3, 4 + br * 3)
                         for c in range(1 + bc * 3, 4 + bc * 3)]
                clauses.append(cells)
                for i in range(len(cells)):
                    for j in range(i + 1, len(cells)):
                        clauses.append([-cells[i], -cells[j]])

    # initial clues
    for r in range(9):
        for c in range(9):
            d = grid[r][c]
            if d != 0:
                clauses.append([varnum(r + 1, c + 1, d)])

    return clauses

def solve_sudoku(grid):
    clauses = sudoku_encode(grid)
    solution = sat_solver.solve_sat(clauses, {})
    if solution is None:
        return None

    # reconstruct grid
    solved = [[0 for _ in range(9)] for _ in range(9)]
    for var, val in solution.items():
        if val:
            r, c, d = decode_var(var)
            solved[r][c] = d
    return solved

# testing:
if __name__ == "__main__":
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    solution = solve_sudoku(puzzle)
    if solution:
        for row in solution:
            print(row)
    else:
        print("No solution found.")
