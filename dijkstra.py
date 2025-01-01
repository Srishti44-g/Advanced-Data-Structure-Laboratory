from priority_queue import PriorityQueue
from collections import defaultdict

class Graph:
    """Graph implementation for Dijkstra's algorithm"""
    
    def __init__(self):
        self.graph = defaultdict(list)
        
    def add_edge(self, src, dest, weight):
        """Add an edge to the graph"""
        self.graph[src].append((dest, weight))
        self.graph[dest].append((src, weight))  # For undirected graph
        
    def dijkstra(self, start):
        """
        Implement Dijkstra's algorithm for shortest path
        
        Args:
            start: Starting vertex
            
        Returns:
            dict: Shortest distances to all vertices
        """
        # Initialize distances
        distances = {vertex: float('infinity') for vertex in self.graph}
        distances[start] = 0
        
        # Priority queue to store vertices and their distances
        pq = PriorityQueue()
        pq.insert((0, start))  # (distance, vertex)
        
        # Track visited vertices
        visited = set()
        
        while len(visited) < len(self.graph):
            # Get vertex with minimum distance
            current_distance, current_vertex = pq.extract_min()
            
            if current_vertex in visited:
                continue
                
            visited.add(current_vertex)
            
            # Update distances to neighbors
            for neighbor, weight in self.graph[current_vertex]:
                if neighbor not in visited:
                    distance = current_distance + weight
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        pq.insert((distance, neighbor))
                        
        return distances

# Test implementation
if __name__ == "__main__":
    g = Graph()
    # Add edges to the graph
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 2)
    g.add_edge('B', 'C', 1)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 8)
    g.add_edge('C', 'E', 10)
    g.add_edge('D', 'E', 2)
    
    start_vertex = 'A'
    distances = g.dijkstra(start_vertex)
    
    print(f"Shortest distances from vertex {start_vertex}:")
    for vertex, distance in distances.items():
        print(f"To {vertex}: {distance}") 