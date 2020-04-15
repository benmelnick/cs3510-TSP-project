import sys
from annealing import *

def main():
    # problem set up - parse command line params
    input_data = sys.argv[1]
    # todo: parse output file command line arg
    output_file = sys.argv[2]
    max_time = int(sys.argv[3])
    

    sa = SimulatedAnneal(input_data, max_time)
    best_path, best_cost = sa.tsp_annealing()

    print("---------best path---------")
    print(best_path)
    print("---------best cost---------")
    print(best_cost)

    # todo: print results to output txt file
    # write best path and best cost into the mat-output.txt file
    with open(output_file, 'w') as file:
        file.write('Best cost: ' + str(best_cost) + '\nBest path: ' + str(best_path))

if __name__ == "__main__":
    main()