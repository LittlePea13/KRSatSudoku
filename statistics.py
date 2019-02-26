import matplotlib.pyplot as plt
import numpy as np
from heuristics import get_block, get_column, get_row
class StatCollector:
    def __init__(self):
        self.n_split = 0

        self.split_2_sat = {}

        self.last_split = []
        self.max_split = {}
        
    def update_stats(self, clauses, variables):
        pos = [1 for variable, value in variables.items() if value == 1]
        self.split_2_sat[self.n_split] = len(pos)
        
    def print_stats(self, printing = True):
        if printing:
            print('#Splits: {}'.format(self.n_split))

        if len(self.last_split) == 0:
            self.last_split = [100]
        last_split_data = {'split': self.last_split[-1], 'row': get_row(abs(self.last_split[-1])), 'column': get_column(abs(self.last_split[-1])), 'block': get_block(abs(self.last_split[-1]))}
        max_row_split_data = sorted(self.last_split, key=lambda x: get_row(abs(x)))[-1]
        max_column_split_data = sorted(self.last_split, key=lambda x: get_column(abs(x)))[-1]
        max_block_split_data = sorted(self.last_split, key=lambda x: get_block(abs(x)))[-1]
        self.max_split = {'max_row': get_row(abs(max_row_split_data)), 'max_column': get_column(abs(max_column_split_data)), 'max_block':  get_block(abs(max_block_split_data))}
        if printing:
            print('Last Split: {}'.format(last_split_data))
            print('Max row in a Split: ', get_row(abs(max_row_split_data)),' Max column in a Split: ', get_column(abs(max_column_split_data)),' Max block in a Split: ', get_block(abs(max_block_split_data)))
            plt.plot(list(self.split_2_sat.keys()),list(self.split_2_sat.values()))
            plt.show()