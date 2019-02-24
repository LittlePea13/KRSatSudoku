import matplotlib.pyplot as plt
class StatCollector:
    def __init__(self):
        self.n_split = 0
        #self.n_backtrack = 0
        #self.n_flip = 0
        
        self.split_2_sat = {}
        #self.flip_2_unit = {}
        #self.flip_2_pure = {}
    
    def update_stats(self, clauses, variables):
        pos = [1 for variable, value in variables.items() if value == 1]
        self.split_2_sat[self.n_split] = len(pos)
        
    def print_stats(self):
        print('#Splits: {}'.format(self.n_split))
        #print('#Backtracks: {}'.format(self.n_backtrack))
        #print('#Flips: {}'.format(self.n_flip))
        #TODO make it fancy
        plt.plot(list(self.split_2_sat.keys()),list(self.split_2_sat.values()))
        plt.show()
