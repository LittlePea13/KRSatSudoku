import os
import sys

def sudoku2dimacs(input_path, output_path):
    '''
    Converts a sudoku file line-by-line to DIMACS format into individual puzzles
    '''
    with open(input_path, 'r') as f:
        for file_id, line in enumerate(f):
            variables = []
            for idx, char in enumerate(line.strip()):
                if char != '.':
                    row = str(int(idx/9) + 1)
                    column = str(idx%9 + 1)
                    variables.append(row + column + char)

            with open('{}/{}_{}.txt'.format(output_path,os.path.splitext(os.path.basename(input_path))[0], file_id), 'w') as output:
                output.write('p cnf {} {}\n'.format(len(variables), len(variables)))
                for var in variables:
                    output.write(var + ' 0\n')

if __name__ == '__main__':
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    sudoku2dimacs(input_path, output_path)
