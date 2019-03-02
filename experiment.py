from heuristics import Random_split, DLCS, Jeroslow_wang, Row_wise_lenght, Column_wise_lenght, Block_wise_lenght, Row_wise_rand, \
    Column_wise_rand, Block_wise_rand, Row_wise, Column_wise, Block_wise
from dl import Davis_Putnam
import sys
import os
import pandas as pd



def experiment(sudoku_path, heur):
    if heur == 'DLCS' or heur is None:
        heuristics = DLCS
    elif heur == 'Jeroslow_wang':
        heuristics = Column_wise_lenght
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


    result_df = pd.DataFrame(columns=['satisfied', 'time', 'n_iter', 'n_split', 'n_backtrack' 'vis_row', 'vis_column', 'vis_block', 'max_depth' ,'avg_depth'])
    all_len = len(os.listdir(sudoku_path))
    for idx, filename in enumerate(os.listdir(sudoku_path)):
        sudoku_file = sudoku_path + filename

        sat_result, time, stat_collector = Davis_Putnam(sudoku_file, heuristics, print_results=False)
        stats = stat_collector.get_results()
        result_list = [sat_result, time] + list(stats)
        result_df = result_df.append(pd.Series(result_list, index=result_df.columns ), ignore_index=True)

        if (idx % 2200) == 0:
            print('{} is done with {}/{}'.format(heur,idx+1, all_len))
    result_df.to_csv('{}.result.csv'.format(heur))
