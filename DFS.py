class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
    
    def dfs_util(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=" ")
        
        if vertex in self.graph:
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    self.dfs_util(neighbor, visited)
    
    def dfs(self, start):
        visited = set()
        self.dfs_util(start, visited)

# Example usage:
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    
    print("DFS starting from vertex 2:")
    g.dfs(2)
