from heuristics import get_block, get_column, get_row
from collections import namedtuple
import math

TimeStamp = namedtuple('TimeStamp', ['iter', 'split','backtrack', 'sat','row','column','block', 'depth'])

class StatCollector:
    def __init__(self):        
        self.history = []
        
        self.n_split = 0
        self.n_backtrack = 0
        self.n_iter = 0
        self.depth = 0

        self.row = set()
        self.column = set()
        self.block = set()

        self.last_split = []
        self.max_split = {}
    
    def create_timestamp(self, variables):
        self.n_iter += 1
        sat = self.get_satisfied(variables)
        new_record = TimeStamp(self.n_iter, self.n_split, self.n_backtrack, sat, len(self.row), len(self.column), len(self.block), self.depth)
        self.history.append(new_record)
    
    def get_satisfied(self, variables):
        return sum(pos_literal for pos_literal in variables.values() if pos_literal > 0)

    def split(self, split_var):
        self.n_split += 1
        self.depth += 1

        r, c, _ = str(split_var)
        b = (int(math.ceil(int(r)/3))-1)*3 + int(math.ceil(int(c)/3))

        self.row.add(int(r))
        self.column.add(int(c))
        self.block.add(int(b))

    def backtrack(self):
        self.n_backtrack += 1
        self.depth = 0
    
    def get_results(self):
        last_ts = self.history[-1]
        depths = [ts.depth for ts in self.history]
        max_depth = max(depths)
        avg_depth = sum(depths) / len(depths)

        return last_ts.iter, last_ts.split, last_ts.backtrack, last_ts.row, last_ts.column, last_ts.block, max_depth, avg_depth
        
    def print_stats(self, printing = True):
        if printing == True:
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