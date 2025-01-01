class BTreeNode:
    def __init__(self, leaf=True):
        self.leaf = leaf
        self.keys = []
        self.children = []

class BTree:
    """Implementation of B-tree"""
    
    def __init__(self, t):
        """Initialize B-tree with minimum degree t"""
        self.root = BTreeNode()
        self.t = t  # Minimum degree
        
    def insert(self, key):
        """Insert a key into the B-tree"""
        root = self.root
        
        # If root is full, create new root
        if len(root.keys) == (2 * self.t) - 1:
            new_root = BTreeNode(leaf=False)
            self.root = new_root
            new_root.children.append(root)
            self._split_child(new_root, 0)
            self._insert_non_full(new_root, key)
        else:
            self._insert_non_full(root, key)
            
    def _split_child(self, parent, i):
        """Split the i-th child of parent"""
        t = self.t
        child = parent.children[i]
        new_node = BTreeNode(leaf=child.leaf)
        
        # Move keys and children
        parent.keys.insert(i, child.keys[t-1])
        parent.children.insert(i + 1, new_node)
        
        new_node.keys = child.keys[t:]
        child.keys = child.keys[:t-1]
        
        if not child.leaf:
            new_node.children = child.children[t:]
            child.children = child.children[:t]
            
    def _insert_non_full(self, node, key):
        """Insert key into non-full node"""
        i = len(node.keys) - 1
        
        if node.leaf:
            # Insert key into leaf node
            while i >= 0 and key < node.keys[i]:
                i -= 1
            node.keys.insert(i + 1, key)
        else:
            # Find appropriate child
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            
            if len(node.children[i].keys) == (2 * self.t) - 1:
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1
                    
            self._insert_non_full(node.children[i], key)
            
    def search(self, key, node=None):
        """Search for a key in the B-tree"""
        if node is None:
            node = self.root
            
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
            
        if i < len(node.keys) and key == node.keys[i]:
            return (node, i)
            
        if node.leaf:
            return None
            
        return self.search(key, node.children[i])

# Test implementation
if __name__ == "__main__":
    btree = BTree(3)  # Minimum degree = 3
    
    # Insert keys
    keys = [10, 20, 5, 6, 12, 30, 7, 17, 25, 22, 16]
    print("Inserting keys:", keys)
    for key in keys:
        btree.insert(key)
        
    # Search for keys
    search_keys = [6, 12, 15]
    for key in search_keys:
        result = btree.search(key)
        if result:
            print(f"Key {key} found")
        else:
            print(f"Key {key} not found") 