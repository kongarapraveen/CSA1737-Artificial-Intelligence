from itertools import permutations

def calculate_total_distance(order, distances):
    total_distance = 0
    num_cities = len(order)
    for i in range(num_cities):
        city1 = order[i]
        city2 = order[(i + 1) % num_cities]
        total_distance += distances[city1][city2]
    return total_distance

def traveling_salesman_brute_force(distances):
    num_cities = len(distances)
    all_cities = range(num_cities)
    min_distance = float('inf')
    best_order = None
    
    for order in permutations(all_cities):
        current_distance = calculate_total_distance(order, distances)
        if current_distance < min_distance:
            min_distance = current_distance
            best_order = order
    
    return best_order, min_distance

# Example usage:
if __name__ == "__main__":
    # Example distances between cities (0-indexed)
    distances = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    
    best_order, min_distance = traveling_salesman_brute_force(distances)
    print(f"Best order of cities: {best_order}")
    print(f"Minimum distance: {min_distance}")
