from experiment import experiment
from multiprocessing import Pool

heurs = ['DLCS', 'Jeroslow_wang', 'Row_wise_lenght']

sudoku_path = ['all_sudokus/' for i in range(len(heurs))]


if __name__=='__main__':
    p = Pool(3)
    p.starmap(experiment,zip(sudoku_path, heurs))
    