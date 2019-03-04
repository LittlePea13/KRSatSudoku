# KRSatSudoku

### Usage:  
./SAT -S{0,1,2,3,4,5,6,7,8,9,10,11} input_file 
### Available heuristics:
(General SAT solver)  
S0: Davis-Putnam algorithm  
S1: DLCS  
S2: Jeroslow_wang (modified)  

(Only with Sudoku problems in format as given in sudoku-rules.txt  
S3: Row_wise_lenght  
S4: Column_wise_lenght  
S5: Block_wise_lenght  
S6: Row_wise_rand  
S7: Column_wise_rand  
S8: Block_wise_rand  
S9: Row_wise  
S10: Column_wise  
S11: Block_wise  

input_file: in DIMACS format

### Experiments:  
Solve sudokus with implemented heuristics and compare results with statistical methods.  
(Note: Pandas is required to run.)
