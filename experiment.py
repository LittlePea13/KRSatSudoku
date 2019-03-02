from heuristics import Random_split, DLCS, Jeroslow_wang, Row_wise_lenght, Column_wise_lenght, Block_wise_lenght, Row_wise_rand, \
    Column_wise_rand, Block_wise_rand, Row_wise, Column_wise, Block_wise
from dl import Davis_Putnam
import sys
import os
import pandas as pd
from multiprocessing import Pool

def experiment(sudoku_path, heur, checkpoint = True):
    if heur == 'DLCS' or heur is None:
        heuristics = DLCS
    elif heur == 'Jeroslow_wang':
        heuristics = Jeroslow_wang
    elif heur == 'Row_wise_lenght':
        heuristics = Row_wise_lenght
    elif heur == 'Column_wise_lenght':
        heuristics = Column_wise_lenght
    elif heur == 'Block_wise_lenght':
        heuristics = Block_wise_lenght
    elif heur == 'Block_wise':
        heuristics = Block_wise
    elif heur == 'Row_wise':
        heuristics = Row_wise
    elif heur == 'Column_wise':
        heuristics = Column_wise
    elif heur == 'Block_wise_rand':
        heuristics = Block_wise_rand
    elif heur == 'Row_wise_rand':
        heuristics = Row_wise_rand
    elif heur == 'Column_wise_rand':
        heuristics = Column_wise_rand
    elif heur == 'Random_split':
        heuristics = Random_split
    else:
        print('wrong heuristics')
        return 


    
    sudoku_list = os.listdir(sudoku_path)
    all_len = len(sudoku_list)

    result_df = pd.DataFrame(columns=['satisfied', 'time', 'n_iter', 'n_split', 'n_backtrack', 'vis_row', 'vis_column', 'vis_block', 'max_depth' ,'avg_depth'])
 
    if checkpoint == True:
        starting_point = find_latest_checkpoint(heur)
        if starting_point != 0:
            result_df = pd.read_csv('{}.result.checkpoint_{}.csv'.format(heur,starting_point),index_col='Unnamed: 0')
        print('{} is starting at {}'.format(heur, starting_point+1))

       
    #for idx, filename in enumerate(sudoku_list[starting_point:],starting_point):
       # sudoku_file = sudoku_path + filename

    pool = Pool(64)
    idx = 0
    dp_input = [(sudoku_path+filename, heuristics, False) for filename in sudoku_list]
        #sat_result, time, stat_collector = Davis_Putnam(sudoku_file, heuristics, print_results=False)
    sat_result, time, stat_collector = pool.starmap(Davis_Putnam, dp_input)
    idx += 1
    stats = stat_collector.get_results()
    result_list = [sat_result, time] + list(stats)
    result_df = result_df.append(pd.Series(result_list, index=result_df.columns ), ignore_index=True)

    if (idx % int(all_len*0.1)) == 0 and idx > 0:
        print('{} is done with {}/{}'.format(heur,idx+1, all_len))
        if checkpoint == True:
            result_df.to_csv('{}.result.checkpoint_{}.csv'.format(heur,idx))

    print('{} is done'.format(heur))
    result_df.to_csv('{}.result.csv'.format(heur))


def find_latest_checkpoint(heur):
    checkpoint_to_filename = {}
    for filename in os.listdir('.'):
        split_file = filename.split('.')
        if split_file[-1] == 'csv' and split_file[0] == heur:
            if len(split_file[-2].split('_')) == 2:
                ckp = int(split_file[-2].split('_')[1])
            else:
                ckp = 0
            checkpoint_to_filename[ckp] = filename
    if len(checkpoint_to_filename) == 0:
        return 0
    else:
        return max(list(checkpoint_to_filename.keys()))

if __name__=='__main__':
    sudoku_path = "all_sudokus/"
    heur = 'DLCS'
    experiment(sudoku_path, heur,checkpoint=True)