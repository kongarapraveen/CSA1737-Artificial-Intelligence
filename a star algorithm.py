import heapq

class Graph:
    def __init__(self):
        self.edges = {}
        self.heuristic = {}
    
    def add_edge(self, node1, node2, cost):
        if node1 not in self.edges:
            self.edges[node1] = []
        self.edges[node1].append((node2, cost))
        
        if node2 not in self.edges:
            self.edges[node2] = []
        self.edges[node2].append((node1, cost))
    
    def set_heuristic(self, node, heuristic_value):
        self.heuristic[node] = heuristic_value
    
    def a_star(self, start, goal):
        open_list = [(0, start)]  # (f_cost, node)
        closed_set = set()
        came_from = {}
        g_score = {node: float('inf') for node in self.edges}
        g_score[start] = 0
        f_score = {node: float('inf') for node in self.edges}
        f_score[start] = self.heuristic[start]
        
        while open_list:
            current_f, current_node = heapq.heappop(open_list)
            
            if current_node == goal:
                path = [current_node]
                while current_node in came_from:
                    current_node = came_from[current_node]
                    path.append(current_node)
                return path[::-1]
            
            closed_set.add(current_node)
            
            for neighbor, cost in self.edges.get(current_node, []):
                if neighbor in closed_set:
                    continue
                
                tentative_g = g_score[current_node] + cost
                if tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current_node
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + self.heuristic[neighbor]
                    heapq.heappush(open_list, (f_score[neighbor], neighbor))
        
        return None

# Example usage:
if __name__ == "__main__":
    graph = Graph()
    
    # Define edges and costs
    graph.add_edge('A', 'B', 1)
    graph.add_edge('A', 'C', 3)
    graph.add_edge('B', 'D', 5)
    graph.add_edge('C', 'D', 1)
    
    # Set heuristic values (for example, using Manhattan distance)
    graph.set_heuristic('A', 6)
    graph.set_heuristic('B', 4)
    graph.set_heuristic('C', 2)
    graph.set_heuristic('D', 0)
    
    # Perform A* search
    start_node = 'A'
    goal_node = 'D'
    path = graph.a_star(start_node, goal_node)
    
    if path:
        print(f"Shortest path from {start_node} to {goal_node}: {' -> '.join(path)}")
    else:
        print(f"No path found from {start_node} to {goal_node}")
