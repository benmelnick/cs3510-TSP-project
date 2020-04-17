
a. 
   Name:
	Ben Melnick
	Xiaohong Chen
	

   Email:
	bmelnick3@gatech.edu
	xchen671@gatech.edu

   Date of submission:
	April 17 2020

b. 
  annealing.py: Simulated annealing algorithm program, get the best path and the best cost given an input file and a maximum time.
  tsp-3510.py: entry point of the program that parses the input file and other command line arguments, calls annealing.py, which takes in the input file and max time and returns the best path and the best cost on the command console. The solution is printed to both the command line and the output file specified in the command line.
  mat-output.txt: include the best path and the best cost
  mat-test.txt: includes the node-ID (a distinct positive integer) and the x-y coordinates for every node (one row per node).
  README.txt: mentioned the information of the author and how to compile this program in the command line.

c. The command-line: python3 tsp-3510.py <input .txt file> <output .txt> <seconds to run program>
   (the maximum time is 3 minutes).

d.
We generate neighboring states by picking random indices in the list and reversing the order of the nodes in between those two indices, which may limit how optimal the solution can get by generating potentially bad states within the allocated time.

e. 
Since every time the best path and the best cost would be different, we would run the program totally 10 times and get the average TSP cost. Below is the average cost and the standard deviation of running our traveling salesman algorithm for 3 minutes (180 seconds)

run 1: 
[6, 2, 1, 5, 4, 3, 7, 9, 14, 17, 16, 24, 27, 25, 20, 26, 28, 29, 21, 23, 22, 18, 19, 15, 13, 12, 8, 10, 11, 6]
cost: 29499

run 2:
[8, 12, 10, 11, 15, 19, 18, 22, 23, 21, 29, 28, 26, 20, 25, 27, 24, 16, 17, 14, 13, 9, 7, 3, 4, 5, 1, 2, 6, 8]
cost: 28804

run 3:
[4, 5, 1, 2, 6, 8, 12, 10, 11, 15, 19, 18, 22, 23, 21, 29, 28, 26, 20, 25, 27, 24, 16, 17, 14, 13, 9, 7, 3, 4]
cost: 28804

run 4:
[23, 22, 21, 17, 18, 19, 15, 12, 11, 10, 6, 2, 1, 5, 4, 3, 7, 9, 8, 13, 14, 16, 24, 27, 25, 20, 26, 28, 29, 23]
cost: 28147

run 5:
[6, 2, 1, 5, 8, 4, 3, 7, 9, 13, 14, 17, 16, 24, 27, 25, 20, 26, 28, 29, 21, 23, 22, 18, 19, 15, 12, 11, 10, 6]
cost: 28031

run 6:
[6, 2, 1, 5, 4, 3, 7, 9, 8, 12, 13, 14, 17, 16, 24, 27, 25, 20, 26, 28, 29, 21, 23, 22, 18, 19, 15, 11, 10, 6]
cost: 28472

run 7:
[1, 5, 4, 3, 7, 9, 8, 12, 13, 14, 17, 20, 16, 24, 27, 25, 26, 28, 29, 21, 23, 22, 18, 19, 15, 11, 10, 6, 2, 1]
cost: 28191

run 8:
[5, 4, 3, 7, 9, 13, 14, 17, 20, 16, 24, 27, 25, 26, 28, 29, 21, 23, 22, 18, 19, 15, 11, 10, 12, 8, 6, 2, 1, 5]
cost: 28523

run 9:
[17, 16, 24, 27, 25, 20, 26, 28, 29, 21, 23, 22, 18, 19, 15, 11, 10, 12, 8, 6, 2, 1, 5, 4, 3, 7, 9, 13, 14, 17]
cost: 28804

run 10: [3, 4, 8, 5, 1, 2, 6, 10, 11, 12, 13, 15, 19, 18, 22, 23, 21, 29, 28, 17, 20, 26, 25, 27, 24, 16, 14, 9, 7, 3]
cost: 29401


the average cost: 28667.6
the standard deviation: 499.7239683













































	
