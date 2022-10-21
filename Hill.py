from Nodes import Nodes

class HillClimbing:
    def __init__(self, state):
        super().__init__()
        self.start_node = Nodes(state)

    def first_choice(self, max_sidesteps=0):
        current_node = self.start_node
        current_cost = current_node.get_cost()
        moves = 0; side_steps = 0
        while True:
            next_child, next_cost = current_node.first_choice_child()
            if(next_cost > current_cost):
                return current_node.state, current_cost, (next_cost == current_cost), moves
            if(next_cost == current_cost):
                side_steps += 1
                if side_steps > max_sidesteps:
                    return current_node.state, current_cost, (next_cost == current_cost), moves
            else:
                side_steps = 0
            current_node, current_cost = next_child, next_cost
            moves += 1

if __name__ == "__main__":
    # Initial State
    start_state = (4,5,6,3,4,5,6,5)
    print("Initial state:")
    Nodes.visualize(start_state)

    hill = HillClimbing(start_state)
    print("Running Steepest-Ascent:")
    end_state, end_cost, is_plateau, moves = hill.steepest_ascent()
    status = "Plateau reached!" if is_plateau else "Local Minima reached!"
    print(status+" state:{} cost:{}".format(end_state, end_cost))
    Nodes.visualize(end_state)

    print("Running First-Choice (with 100 sidesteps):")
    end_state, end_cost, is_plateau, moves = hill.first_choice(100)
    status = "Plateau reached!" if is_plateau else "Local Minima reached!"
    print(status+" state:{} cost:{}".format(end_state, end_cost))
    Nodes.visualize(end_state)