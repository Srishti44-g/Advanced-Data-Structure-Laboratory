class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}
        
    def find(self, item):
        """Find the set of an item (with path compression)"""
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]
        
    def union(self, x, y):
        """Union of two sets (by rank)"""
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                root_x, root_y = root_y, root_x
            self.parent[root_y] = root_x
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1

class Graph:
    """Graph implementation for Kruskal's algorithm"""
    
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []
        
    def add_edge(self, src, dest, weight):
        """Add an edge to the graph"""
        self.edges.append((src, dest, weight))
        
    def kruskal_mst(self):
        """
        Implement Kruskal's algorithm for Minimum Spanning Tree
        
        Returns:
            list: Edges in the MST
        """
        # Sort edges by weight
        self.edges.sort(key=lambda x: x[2])
        
        # Initialize disjoint set
        ds = DisjointSet(self.vertices)
        
        mst = []
        for edge in self.edges:
            src, dest, weight = edge
            
            # Check if adding edge creates cycle
            if ds.find(src) != ds.find(dest):
                ds.union(src, dest)
                mst.append(edge)
                
        return mst

# Test implementation
if __name__ == "__main__":
    # Create graph
    vertices = ['A', 'B', 'C', 'D', 'E']
    g = Graph(vertices)
    
    # Add edges
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 2)
    g.add_edge('B', 'C', 1)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 8)
    g.add_edge('C', 'E', 10)
    g.add_edge('D', 'E', 2)
    
    # Find MST
    mst = g.kruskal_mst()
    
    print("Minimum Spanning Tree edges:")
    total_weight = 0
    for src, dest, weight in mst:
        print(f"{src} -- {dest} == {weight}")
        total_weight += weight
    print(f"Total MST weight: {total_weight}") 