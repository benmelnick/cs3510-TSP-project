import sys
from annealing import *

def main():
    # problem set up - parse command line params
    input_data = sys.argv[1]
    max_time = int(sys.argv[2])
    # todo: parse output file command line arg

    sa = SimulatedAnneal(input_data, max_time)
    best_path, best_cost = sa.tsp_annealing()

    print("---------best path---------")
    print(best_path)
    print("---------best cost---------")
    print(best_cost)

    # todo: print results to output txt file

if __name__ == "__main__":
    main()