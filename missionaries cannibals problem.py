from collections import deque

class State:
    def __init__(self, missionaries, cannibals, boat):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
    
    def is_valid(self):
        if self.missionaries < 0 or self.cannibals < 0 or self.missionaries > 3 or self.cannibals > 3:
            return False
        if self.missionaries > 0 and self.missionaries < self.cannibals:
            return False
        if self.missionaries < 3 and (3 - self.missionaries) < (3 - self.cannibals):
            return False
        return True
    
    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0 and self.boat == 0
    
    def __eq__(self, other):
        return self.missionaries == other.missionaries and self.cannibals == other.cannibals and self.boat == other.boat
    
    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat))
    
    def __str__(self):
        return f"({self.missionaries}, {self.cannibals}, {self.boat})"

def successors(state):
    children = []
    
    if state.boat == 1:
        for i in range(3):
            for j in range(3):
                if 1 <= i + j <= 2:
                    new_state = State(state.missionaries - i, state.cannibals - j, 0)
                    if new_state.is_valid():
                        children.append(new_state)
    else:
        for i in range(3):
            for j in range(3):
                if 1 <= i + j <= 2:
                    new_state = State(state.missionaries + i, state.cannibals + j, 1)
                    if new_state.is_valid():
                        children.append(new_state)
    return children

def bfs(start):
    if start.is_goal():
        return [start]
    
    queue = deque([[(start)]])
    visited = set()
    visited.add(start)
    
    while queue:
        path = queue.popleft()
        state = path[-1]
        
        for child in successors(state):
            if child not in visited:
                if child.is_goal():
                    return path + [child]
                visited.add(child)
                queue.append(path + [child])
    
    return None

def print_solution(solution):
    if solution is None:
        print("No solution found.")
    else:
        print("Missionaries, Cannibals, Boat")
        for state in solution:
            print(state)

if __name__ == "__main__":
    initial_state = State(3, 3, 1)
    solution = bfs(initial_state)
    print_solution(solution)
