import math
import time
import random

class SimulatedAnneal:
    def __init__(self, file_name, max_time):
        self.coords = []
        self.nodes = []
        file = open(file_name, "r")
        for line in file:
            node_id, x, y = line.split()
            self.coords.append((int(node_id), (float(x), float(y))))
            self.nodes.append(int(node_id))
        file.close()
        self.N = len(self.coords)  # number of nodes in the problem
        self.max_time = max_time
        self.start_time = time.time()
        self.temp = max_time
        self.stopping_temp = 0.00000001

        # compute distances between all possible pairs of nodes
        # dictionary where index is (node a, node b) and value is distance b/w them
        self.distances = {}
        for i in range(len(self.coords) - 1):
            node_a = self.coords[i]
            for j in range(i + 1, len(self.coords)):
                node_b = self.coords[j]
                self.distances[(node_a[0], node_b[0])] = self.compute_distance(node_a[1], node_b[1])

        self.curr_solution, self.curr_cost = self.get_starting_state()
        self.best_path = self.curr_solution
        self.best_cost = self.curr_cost

    def compute_distance(self, a_coord, b_coord):
        """
        Compute distance b/w two nodes
        :param a_coord: (x, y) tuple of coordinates for node a
        :param b_coord: (x, y) tuple of coordinates for node b
        :return: distance b/w nodes a and b
        """
        return int(round(math.sqrt((a_coord[0] - b_coord[0]) ** 2 + (a_coord[1] - b_coord[1]) ** 2)))

    def get_nodes(self):
        return self.nodes

    def get_distances(self):
        return str(self.distances)

    def get_distance(self, a, b):
        """
        find the distance between two nodes kept in self.distances
        self.distances only maintains and finds distances for nodes (a,b) when a < b
        this method will find the distance between two nodes if order is reversed
        :param a: a node id
        :param b: a node id
        :return: distance b/w the nodes
        """
        if (a, b) in self.distances:
            return self.distances[(a, b)]
        if (b, a) in self.distances:
            return self.distances[(b, a)]
        return None

    # create some initial state for the problem that we will attempt to improve over time
    def get_starting_state(self):
        """
        Greedy algorithm to get an initial solution by choosing the closest neighbor
        :return:
        """
        curr_node = self.nodes[0]
        path = [curr_node]
        remaining_nodes = set(self.nodes)
        remaining_nodes.remove(curr_node)

        while remaining_nodes:
            next_node = min(remaining_nodes, key=lambda x: self.get_distance(curr_node, x))
            remaining_nodes.remove(next_node)
            path.append(next_node)
            curr_node = next_node

        print("------initial solution-------")
        print(path)

        # calculate the total cost of the current path
        curr_cost = self.cost(path)
        print("------initial cost--------")
        print(curr_cost)
        # update if necessary

        return path, curr_cost

    def cost(self, path):
        """
        calculate the total distance of the current solution path
        :param path: list of nodes
        :return: total cost
        """
        cost = 0
        for i in range(1, len(path)):
            cost += self.get_distance(path[i - 1], path[i])
        # need to include cost of going from last node to start node in the path
        cost += self.get_distance(path[-1], path[0])
        return cost

    def tsp_annealing(self):
        """
        perform the actual simulated annealing algorithm
        """
        # temp is a function of time passed, so we can use temp as the stopping condition
        while self.temp >= self.stopping_temp:
            time_elapsed = time.time() - self.start_time
            candidate_solution, candidate_cost = self.get_neighboring_state()
            # always take the new state if it provides a lower total cost
            if candidate_cost < self.curr_cost:
                self.curr_cost = candidate_cost
                self.curr_solution = candidate_solution
                if candidate_cost < self.best_cost:
                    self.best_cost = candidate_cost
                    self.best_path = candidate_solution
            # otherwise, accept the new state based on probability
            else:
                if random.random() < self.calculate_acceptance_probability(candidate_cost):
                    self.curr_cost = candidate_cost
                    self.curr_solution = candidate_solution

            # calculate the new temperature
            self.temp = self.calculate_temperature(time_elapsed)
        # start node and end node are the same node
        self.best_path.append(self.best_path[0])

        return self.best_path, self.best_cost

    # produce a neighbor of a state by conservatively altering a given state
    # each state is defined as a permutation of cities to be visited
    # neighbors of a state are the set of permutations produced by reversing the order of any two successive cities
    def get_neighboring_state(self):
        """
        Finding a neighboring state using the 2 opt process
        https://en.wikipedia.org/wiki/2-opt
        :return: a new list of nodes representing a neighboring state
        """
        candidate = list(self.curr_solution)
        k = random.randint(2, self.N - 1)
        i = random.randint(0, self.N - k)

        # first 0 to i-1 nodes stay in tact
        # next i to k nodes are reversed
        # lsat nodes remain in tact
        candidate[i: (i + k)] = reversed(candidate[i: (i + k)])
        candidate_cost = self.cost(candidate)

        return candidate, candidate_cost

    # calculates a time-varying parameter known as temperature
    # plays a role in controlling the evolution of the current state
    # based on time elapsed so far and the total time limit
    def calculate_temperature(self, time_elapsed):
        # 1 - (time elapsed / time limit)
        return 1 - (time_elapsed / self.max_time)

    # calculates the probability of making the transition from current state to a potential new state
    # depends on the total cost of the current and new path and the current temperature value
    def calculate_acceptance_probability(self, new_cost):
        diff_cost = new_cost - self.curr_cost
        # probability should decrease as diff_cost increases and temperature decreases
        if self.temp == 0:
            return 0
        return math.exp((-1 * diff_cost) / self.temp)
