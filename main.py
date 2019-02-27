from heuristics import Random_split, DLCS, Jeroslow_wang
from dl import Davis_Putnam
import sys


if __name__ == '__main__':
    # Example to run: python main.py sudokus/damnhard.sdk_0.txt 1
    filename = sys.argv[1]
    heur = sys.argv[2]
    if heur == '1' or heur is None:
        heuristics = Jeroslow_wang
    else:
        heuristics = DLCS
    Davis_Putnam(filename, heuristics)
