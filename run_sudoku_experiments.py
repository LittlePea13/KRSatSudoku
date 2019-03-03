from experiment import experiment
from multiprocessing import Pool
import heuristics

heurs = ['Random_split', 'DLCS', 'Jeroslow_wang', 'Row_wise_lenght', 'Column_wise_lenght', 'Block_wise_lenght', 'Row_wise_rand', \
    'Column_wise_rand', 'Block_wise_rand', 'Row_wise', 'Column_wise', 'Block_wise']

sudoku_path = ['sudokus/' for i in range(len(heurs))]

if __name__=='__main__':
    p = Pool(len(heurs))
    p.starmap(experiment,zip(sudoku_path, heurs))
    