import heuristics
from dp import davis_putnam
import sys
import os
import pandas as pd


def experiment(sudoku_path, heur, checkpoint = True):

    heuristics_func = getattr(heuristics, heur)

    print(sudoku_path)
    sudoku_list = os.listdir(sudoku_path)
    all_len = len(sudoku_list)

    result_df = pd.DataFrame(columns=['satisfied', 'time', 'n_iter', 'n_split', 'n_backtrack', 'vis_row', 'vis_column', 'vis_block', 'max_depth' ,'avg_depth'])
 
    if checkpoint == True:
        starting_point = find_latest_checkpoint(heuristics_func.__name__)
        if starting_point != 0:
            result_df = pd.read_csv('{}.result.checkpoint_{}.csv'.format(heuristics_func.__name__,starting_point),index_col='Unnamed: 0')
        print('{} is starting at {}'.format(heuristics_func.__name__, starting_point+1))
        
    for idx, filename in enumerate(sudoku_list[starting_point:],starting_point):
        sudoku_file = sudoku_path + filename

        sat_result, time, stat_collector = davis_putnam(sudoku_file, heuristics_func, print_results=False)
        stats = stat_collector.get_results()
        result_list = [sat_result, time] + list(stats)
        result_df = result_df.append(pd.Series(result_list, index=result_df.columns ), ignore_index=True)

        if (idx % int(all_len*0.1)) == 0 and idx > 0:
            print('{} is done with {}/{}'.format(heuristics_func.__name__,idx+1, all_len))
            if checkpoint == True:
                result_df.to_csv('{}.result.checkpoint_{}.csv'.format(heuristics_func.__name__,idx))

    print('{} is done'.format(heuristics_func.__name__))
    result_df.to_csv('{}.result.csv'.format(heuristics_func.__name__))


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
