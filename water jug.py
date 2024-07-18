from collections import deque

def water_jug_problem(jug1_capacity, jug2_capacity, target_liters):
    # Check if target_liters can be achieved
    if target_liters > max(jug1_capacity, jug2_capacity):
        print("Target liters cannot be achieved with given jug capacities.")
        return

    # Initialize visited states and queue for BFS
    visited = set()
    queue = deque([(0, 0)])  # (jug1, jug2)
    visited.add((0, 0))

    while queue:
        jug1, jug2 = queue.popleft()

        # Check if target_liters is achieved
        if jug1 == target_liters or jug2 == target_liters or jug1 + jug2 == target_liters:
            print(f"Target liters ({target_liters}L) can be achieved:")
            print(f"Jug 1: {jug1}L, Jug 2: {jug2}L")
            return True

        # Define all possible operations
        operations = [
            (jug1_capacity, jug2),  # Fill jug1
            (jug1, jug2_capacity),  # Fill jug2
            (0, jug2),  # Empty jug1
            (jug1, 0),  # Empty jug2
            (jug1 - min(jug1, jug2_capacity - jug2), jug2 + min(jug1, jug2_capacity - jug2)),  # Pour jug1 to jug2
            (jug1 + min(jug2, jug1_capacity - jug1), jug2 - min(jug2, jug1_capacity - jug1))   # Pour jug2 to jug1
        ]

        # Try all operations and add new states to the queue if not visited
        for operation in operations:
            new_jug1, new_jug2 = operation
            if (new_jug1, new_jug2) not in visited:
                visited.add((new_jug1, new_jug2))
                queue.append((new_jug1, new_jug2))

    # If queue is exhausted and no solution found
    print(f"Target liters ({target_liters}L) cannot be achieved with given jug capacities.")
    return False

# Example usage:
if __name__ == "__main__":
    jug1_capacity = 4
    jug2_capacity = 3
    target_liters = 2

    water_jug_problem(jug1_capacity, jug2_capacity, target_liters)
