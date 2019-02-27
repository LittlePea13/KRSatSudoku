import matplotlib.pyplot as plt
import numpy as np
from heuristics import get_block, get_column, get_row
from collections import namedtuple

TimeStamp = namedtuple('TimeStamp', ['iter', 'split', 'sat','row','column','block', 'depth'])

class StatCollector:
    def __init__(self):        
        self.history = []
        
        self.n_split = 0
        self.n_iter = 10
        self.depth = 0

        self.row = set()
        self.column = set()
        self.block = set()

        #TODO rewrite this part
        self.split_2_sat = {}
        self.iter_2_split = {}
        self.iter_2_sat = {}

        self.last_split = []
        self.max_split = {}
    
    def create_timestamp(self, variables):
        self.n_iter += 1
        sat = self.get_satisfied(variables)
        new_record = TimeStamp(self.n_iter, self.n_split, sat, len(self.row), len(self.column), len(self.block), self.depth)
        self.history.append(new_record)
    
    def get_satisfied(self, variables):
        return sum(pos_literal for pos_literal in variables.values() if pos_literal > 0)

    def split(self, split_var):
        self.n_split += 1
        self.depth += 1

        r, c, _ = str(split_var)
        #b = 

        self.row.add(r)
        self.column.add(c)
        #self.block.add(b)

    def backtrack(self):
        self.depth = 0
        
    def update_stats(self, clauses, variables):
        pos = [1 for variable, value in variables.items() if value == 1]
        self.split_2_sat[self.n_split] = len(pos)
        
    def print_stats(self, printing = True):
        if printing == False:
            print('#Splits: {}'.format(self.n_split))
            print('#Iteration {}'.format(self.n_iter))
            print('#Timestamp {}'.format(len(self.history)))

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