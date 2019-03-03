from heuristics import Random_split, DLCS, Jeroslow_wang, Row_wise_lenght, Column_wise_lenght, Block_wise_lenght
from dp import davis_putnam
import sys


if __name__ == '__main__':
    # Example to run: python main.py sudokus/damnhard.sdk_0.txt 1
    filename = sys.argv[1]
    heur = sys.argv[2]
    if heur == '1' or heur is None:
        heuristics = Row_wise_lenght
    elif heur == '2':
        heuristics = Column_wise_lenght
    elif heur == '3':
        heuristics = Block_wise_lenght
    davis_putnam(filename, heuristics)
