from collections import deque

# Defining the bucket capacities
CAPACITIES = (8, 5, 3)

# Function to perform the BFS search
def bfs():
    # Initial state with the 8-liter bucket full, the others empty
    initial_state = (8, 0, 0)
    # The queue will store states and their associated moves
    queue = deque([(initial_state, [])])
    # To prevent revisiting the same state
    visited = set()
    visited.add(initial_state)

    while queue:
        current_state, path = queue.popleft()
        if 4 in current_state:  # If one of the buckets has exactly 4 liters, solution found
            return path + [current_state]

        # Generate all possible next states
        for i in range(3):  # Choose a bucket to pour from
            for j in range(3):  # Choose a bucket to pour into
                if i != j:
                    next_state = list(current_state)
                    # Determine how much water can be transferred
                    amount_to_pour = min(next_state[i], CAPACITIES[j] - next_state[j])
                    next_state[i] -= amount_to_pour
                    next_state[j] += amount_to_pour
                    next_state_tuple = tuple(next_state)
                    if next_state_tuple not in visited:
                        visited.add(next_state_tuple)
                        queue.append((next_state_tuple, path + [current_state]))

    return None  # No solution found

# Function to print the solution path
def print_solution():
    solution = bfs()
    if solution:
        print("Solution found with the following moves:")
        for step, state in enumerate(solution):
            print(f"Step {step}: Buckets state {state}")
    else:
        print("No solution found.")

# Run the solver
print_solution()
#sample output
'''Solution found with the following moves:
Step 0: Buckets state (8, 0, 0)
Step 1: Buckets state (3, 5, 0)
Step 2: Buckets state (3, 2, 3)
Step 3: Buckets state (6, 2, 0)
Step 4: Buckets state (6, 0, 2)
Step 5: Buckets state (1, 5, 2)
Step 6: Buckets state (1, 4, 3)
'''