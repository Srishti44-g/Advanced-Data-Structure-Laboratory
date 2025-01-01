class HashTable:
    """Implementation of Hash Table using linear probing"""
    
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
        self.count = 0
        
    def _hash(self, key):
        """Hash function"""
        if isinstance(key, str):
            # For strings, use sum of ASCII values
            return sum(ord(c) for c in key) % self.size
        return key % self.size
        
    def _probe(self, index):
        """Linear probing"""
        return (index + 1) % self.size
        
    def insert(self, key, value):
        """Insert a key-value pair"""
        if self.count >= self.size:
            raise IndexError("Hash table is full")
            
        index = self._hash(key)
        while self.table[index] is not None:
            # If key already exists, update value
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = self._probe(index)
            
        self.table[index] = (key, value)
        self.count += 1
        
    def get(self, key):
        """Get value for a key"""
        index = self._hash(key)
        original_index = index
        
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = self._probe(index)
            if index == original_index:
                break
                
        raise KeyError(f"Key '{key}' not found")
        
    def remove(self, key):
        """Remove a key-value pair"""
        index = self._hash(key)
        original_index = index
        
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                self.count -= 1
                return
            index = self._probe(index)
            if index == original_index:
                break
                
        raise KeyError(f"Key '{key}' not found")
        
    def __str__(self):
        return str([item for item in self.table if item is not None])

# Test implementation
if __name__ == "__main__":
    ht = HashTable()
    
    print("Inserting key-value pairs:")
    pairs = [
        ("apple", 5),
        ("banana", 8),
        ("orange", 3),
        ("grape", 2)
    ]
    
    for key, value in pairs:
        ht.insert(key, value)
        print(f"Inserted: {key} -> {value}")
    
    print("\nHash Table:", ht)
    
    print("\nGetting values:")
    for key, _ in pairs:
        print(f"{key} -> {ht.get(key)}")
    
    remove_key = "banana"
    print(f"\nRemoving '{remove_key}'")
    ht.remove(remove_key)
    print("Hash Table after removal:", ht) 