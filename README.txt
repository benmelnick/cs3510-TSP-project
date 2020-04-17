
a. 
   Name:
	Ben Melnick
	Xiaohong Chen
	

   Email:
	bmelnick3@gatech.edu
	xchen671@gatech.edu

   Date of submission:
	April 16 2020

b. 
  annealing.py: Simulated annealing algorithm program, get the best path and 		  the best cost.
  tsp-3510.py: a function that running the annealing.py file where the inputs 		 come, display the best path and the best cost on the command 			 console and write the best path, best cost into the 
		 mat-output.txt file.
  mat-output.txt: include the best path and the best cost
  mat-test.txt: includes the node-ID (a distinct positive integer) and the x-y  		  coordinates for every node (one row per node).
  README.txt: mentioned the information of the author and how to compile this 		program in the command line.

c. The command-line: python3 tsp-3510.py mat-test.txt mat-output.txt 3
   (the maximum time is 3 minutes).

d.
# todo: if there are more bugs or the limited exist
we generate neighboring states by picking random indices in the list and reversing the order of the nodes in  between those two indices, which may limit how optimal the solution can get by generating potentially bad states within the alloted time.

e. 
since every time the best path and the best cost would be different, we 	would run the program totally 10 times and get the average TSP cost. 	Meanwhile, calculate the standard deviation of the cost.

run 1: 
[8, 12, 10, 11, 15, 19, 18, 22, 23, 21, 29, 28, 26, 20, 25, 27, 24, 16, 17, 14, 13, 9, 7, 3, 4, 5, 1, 2, 6, 8]
cost: 28804

run 2:
[2, 1, 5, 4, 3, 7, 9, 8, 12, 13, 14, 16, 24, 27, 25, 26, 20, 17, 28, 29, 21, 23, 22, 18, 19, 15, 11, 10, 6, 2]
cost: 28855

run 3:
[12, 13, 14, 17, 16, 24, 27, 25, 20, 26, 28, 29, 21, 23, 22, 18, 19, 15, 11, 10, 6, 2, 1, 5, 4, 3, 7, 9, 8, 12]
cost: 28472

run 4:
[15, 19, 18, 22, 23, 21, 29, 28, 17, 20, 26, 25, 27, 24, 16, 14, 13, 9, 7, 3, 4, 5, 1, 2, 6, 8, 12, 10, 11, 15]
cost: 29187

run 5:
[17, 14, 13, 8, 9, 7, 3, 4, 5, 1, 2, 6, 10, 11, 12, 15, 19, 18, 22, 23, 21, 29, 28, 26, 25, 27, 24, 16, 20, 17]
cost: 28294

run 6:
[13, 14, 17, 16, 24, 27, 25, 20, 26, 28, 29, 21, 23, 22, 18, 19, 15, 11, 10, 12, 8, 6, 2, 1, 5, 4, 3, 7, 9, 13]
cost: 28804

run 7:
[15, 12, 11, 10, 6, 2, 1, 5, 8, 4, 3, 7, 9, 13, 14, 17, 16, 24, 27, 25, 20, 26, 28, 29, 21, 23, 22, 18, 19, 15]
cost: 28031

run 8:
[25, 20, 26, 28, 29, 21, 23, 22, 18, 19, 15, 13, 12, 11, 10, 6, 2, 1, 5, 8, 4, 3, 7, 9, 14, 17, 16, 24, 27, 25]
cost: 29018

run 9: 
[8, 12, 10, 11, 15, 19, 18, 22, 23, 21, 29, 28, 17, 20, 26, 25, 27, 24, 16, 14, 13, 9, 7, 3, 4, 5, 1, 2, 6, 8]
cost: 29187

run 10:
[29, 21, 23, 22, 18, 19, 15, 11, 10, 12, 8, 6, 2, 1, 5, 4, 3, 7, 9, 13, 14, 17, 16, 24, 27, 25, 20, 26, 28, 29]
cost: 28804

the average cost: 28745.6
the standard deviation: 376.463426













































	
