import numpy as np
from HillClimbing import HillClimbing
from SimulatedAnnealing import SimulatedAnnealing
import warnings
import sys

NUM_STATES = 1000

def generate_state():
    return np.random.randint(8, size=8)

def print_results(num_moves):
    print("\nResults:")
    for algo_name, moves in num_moves.items():
        print(algo_name)
        print('-'*15)
        result_string = "Solved {}/{} cases ({:.2f}%).\nAverage # of moves to find soln:{:.2f}\n"\
                        .format(len(moves), NUM_STATES, len(moves)/NUM_STATES*100, np.mean(moves))
        print(result_string)

def update_progress(progress, total):
    percent  = progress/total*100
    sys.stdout.write('\r[{}] {:.2f}% {}/{} cases'.format('#'*int(percent/5)+'-'*(20-int(percent/5)), percent, progress, total))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            NUM_STATES = int(sys.argv[0])
        except:
            print("This runs the algorithms on 1000 initial states.")
            sys.exit()
    np.random.seed(42)

    algos = [ "Hill climbing steepest ascent",'Hill climbing', 'Hill climbing sideways move']
    num_moves = {algo: [] for algo in algos}

    # Generate random state
    states = [generate_state() for i in range(NUM_STATES)]
    print("Running algorithms...")
    for i, state in enumerate(states):
        # Solve with Hill Climbing
        hill = HillClimbing(state)
        # Steepest Ascent
        end_state, end_cost, is_plateau, moves = hill.steepest_ascent()
        if(end_cost == 0): num_moves[algos[0]].append(moves)

        # First Choice
        end_state, end_cost, is_plateau, moves = hill.first_choice()
        if(end_cost == 0): num_moves[algos[1]].append(moves)
        # First Choice (max. 100 sideways moves)
        # end_state, end_cost, is_plateau, moves = hill.first_choice(100)
        # if(end_cost == 0): num_moves[algos[2]].append(moves)

        # sim = SimulatedAnnealing(state)
        # Simulated Annealing
        # end_state, end_cost, moves = sim.solve()
        # if(end_cost == 0): num_moves[algos[3]].append(moves)

        update_progress(i+1, NUM_STATES)

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)
        print_results(num_moves)