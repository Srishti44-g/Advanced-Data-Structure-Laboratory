class PriorityQueue:
    """Implementation of Priority Queue ADT using a binary heap"""
    
    def __init__(self):
        self.heap = []
        
    def parent(self, i):
        """Get parent index"""
        return (i - 1) // 2
        
    def left_child(self, i):
        """Get left child index"""
        return 2 * i + 1
        
    def right_child(self, i):
        """Get right child index"""
        return 2 * i + 2
        
    def swap(self, i, j):
        """Swap elements at indices i and j"""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        
    def insert(self, key):
        """Insert a new key into the priority queue"""
        self.heap.append(key)
        self._sift_up(len(self.heap) - 1)
        
    def _sift_up(self, i):
        """Move a node up to its proper position"""
        parent = self.parent(i)
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.swap(i, parent)
            self._sift_up(parent)
            
    def extract_min(self):
        """Remove and return the minimum element"""
        if len(self.heap) == 0:
            raise IndexError("Priority queue is empty")
            
        if len(self.heap) == 1:
            return self.heap.pop()
            
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        
        return min_val
        
    def _sift_down(self, i):
        """Move a node down to its proper position"""
        min_index = i
        left = self.left_child(i)
        right = self.right_child(i)
        
        if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left
            
        if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right
            
        if i != min_index:
            self.swap(i, min_index)
            self._sift_down(min_index)
            
    def __str__(self):
        return str(self.heap)

# Test implementation
if __name__ == "__main__":
    pq = PriorityQueue()
    print("Inserting: 5, 2, 8, 1, 9")
    pq.insert(5)
    pq.insert(2)
    pq.insert(8)
    pq.insert(1)
    pq.insert(9)
    print("Priority Queue:", pq)
    
    print("\nExtracting minimum elements:")
    for _ in range(3):
        print("Extracted:", pq.extract_min())
        print("Priority Queue:", pq) 