from Node import Node 
from math import log10, exp, log
from numpy.random import rand

class SimulatedAnnealing:
    MAX_TIME = 500

    def __init__(self, state):
        super().__init__()
        self.start_node = Node(state)

    def schedule(self, time):
        if time > self.MAX_TIME: return 0
        if(time == 0): time = 1e-10
        return 503/(time**3)
        # return 1000/10**(time+1)
        # return 0.01/log10(time+1)

    def solve(self):
        current_node = self.start_node
        current_cost = current_node.get_cost()
        next_cost = current_cost
        time = 0
        num1=0
        while True:
            T = self.schedule(time)
            if T == 0:
                break
            next_child, next_cost = current_node.random_child() 
            dE = (current_cost - next_cost) # Opposite sign cuz we have cost instead of value
            if dE > 0 or rand() < exp(dE/T):
                num1 += 1
                current_node, current_cost = next_child, next_cost
                if next_cost == 0:
                    break
            time += 1
        # print("Option 1:{}, Option 2:{}".format(num1, time-num1))
        return current_node.state, current_cost, time

if __name__ == "__main__":
    # Initial state
    start_state = (4,5,6,3,4,5,6,5)
    print("Initial state:")
    Node.visualize(start_state)

    print("Running Simulated-Annealing:")
    sim = SimulatedAnnealing(start_state)
    end_state, end_cost, moves = sim.solve()
    status = "Solution found!" if end_cost == 0 else "Annealing Ended."
    print(status+" state:{} cost:{}".format(end_state, end_cost))
    Node.visualize(end_state)
