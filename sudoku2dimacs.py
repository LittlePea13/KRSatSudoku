import os
import sys

def sudoku2dimacs(filename):
    '''
    Converts a sudoku file line-by-line to DIMACS format into individual puzzles
    '''
    with open(filename, 'r') as f:
        for file_id, line in enumerate(f):
            variables = []
            for idx, char in enumerate(line.strip()):
                if char != '.':
                    row = str(int(idx/9) + 1)
                    column = str(idx%9 + 1)
                    variables.append(row + column + char)

            with open('sudokus/{}_{}.txt'.format(os.path.splitext(filename)[0], file_id), 'w') as output:
                output.write('p cnf {} {}\n'.format(len(variables), len(variables)))
                for var in variables:
                    output.write(var + '0 \n')

if __name__ == '__main__':
    filename = sys.argv[1]
    sudoku2dimacs(filename)
