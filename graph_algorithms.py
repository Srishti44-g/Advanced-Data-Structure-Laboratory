from collections import defaultdict, deque

class Graph:
    """Graph implementation with BFS and DFS traversals"""
    
    def __init__(self):
        self.graph = defaultdict(list)
        
    def add_edge(self, src, dest):
        """Add an edge to the graph"""
        self.graph[src].append(dest)
        
    def bfs(self, start):
        """
        Breadth First Search traversal
        
        Args:
            start: Starting vertex
            
        Returns:
            list: BFS traversal order
        """
        visited = set()
        queue = deque([start])
        result = []
        
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                
                # Add unvisited neighbors to queue
                queue.extend(v for v in self.graph[vertex] if v not in visited)
                
        return result
        
    def dfs_recursive(self, vertex, visited=None, result=None):
        """
        Recursive Depth First Search traversal
        
        Args:
            vertex: Current vertex
            visited: Set of visited vertices
            result: List to store traversal order
            
        Returns:
            list: DFS traversal order
        """
        if visited is None:
            visited = set()
        if result is None:
            result = []
            
        visited.add(vertex)
        result.append(vertex)
        
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited, result)
                
        return result
        
    def dfs_iterative(self, start):
        """
        Iterative Depth First Search traversal
        
        Args:
            start: Starting vertex
            
        Returns:
            list: DFS traversal order
        """
        visited = set()
        stack = [start]
        result = []
        
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                
                # Add unvisited neighbors to stack
                stack.extend(v for v in reversed(self.graph[vertex]) 
                           if v not in visited)
                
        return result

# Test implementation
if __name__ == "__main__":
    # Create a graph
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    
    start_vertex = 2
    print(f"Graph traversals starting from vertex {start_vertex}:")
    
    print("\nBFS traversal:")
    print(g.bfs(start_vertex))
    
    print("\nDFS traversal (recursive):")
    print(g.dfs_recursive(start_vertex))
    
    print("\nDFS traversal (iterative):")
    print(g.dfs_iterative(start_vertex)) 