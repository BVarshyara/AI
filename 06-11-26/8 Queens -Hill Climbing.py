import random
def calculate_heuristic(state):
    attacks = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j]:
                attacks += 1
            elif abs(state[i] - state[j]) == j - i:
                attacks += 1
    return attacks
def get_best_neighbor(state):
    n = len(state)
    current_h = calculate_heuristic(state)
    best_neighbor = list(state)
    best_h = current_h
    all_best_neighbors = []
    for col in range(n):
        original_row = state[col]
        for row in range(n):
            if row == original_row:
                continue
            neighbor = list(state)
            neighbor[col] = row
            neighbor_h = calculate_heuristic(neighbor)
            if neighbor_h < best_h:
                best_h = neighbor_h
                all_best_neighbors = [neighbor]
            elif neighbor_h == best_h and neighbor_h < current_h:
                all_best_neighbors.append(neighbor)
    if all_best_neighbors:
        return random.choice(all_best_neighbors), best_h      
    return state, current_h
def hill_climbing_8_queens():
    print("\n========== NEW RESTART ==========")
    state = [random.randint(0, 7) for _ in range(8)]
    current_h = calculate_heuristic(state)
    steps = 0
    print("\nInitial Board:")
    print("Heuristic:", current_h)
    print_board(state)
    while True:
        neighbor, neighbor_h = get_best_neighbor(state)
        if neighbor_h >= current_h:
            print("\nNo better neighbor found!")
            print("Reached Local Minimum / Plateau.")
            break
        state = neighbor
        current_h = neighbor_h
        steps += 1
        print(f"\nStep {steps}:")
        print("Heuristic:", current_h)
        print_board(state)
    return state, current_h, steps
def solve_with_random_restart():
    restart_count = 0
    total_steps = 0
    print("Searching for a solution...")
    while True:
        state, final_h, steps = hill_climbing_8_queens()
        total_steps += steps
        if final_h == 0:
            print(f"\n🎉 Success! Found a valid solution.")
            print(f"Total Restarts Required: {restart_count}")
            print(f"Total Moves Explored: {total_steps}")
            print_board(state)
            break
        else:
            restart_count += 1
def print_board(state):
    print("\n   Board Configuration:")
    for row in range(8):
        line = ""
        for col in range(8):
            if state[col] == row:
                line += " Q "
            else:
                line += " . "
        print(line)
    print(f"\nState Array Representation: {state}")
if __name__ == "__main__":
    solve_with_random_restart()
