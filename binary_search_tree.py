class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    """Implementation of Binary Search Tree"""
    
    def __init__(self):
        self.root = None
        
    def insert(self, key):
        """Insert a key into the BST"""
        self.root = self._insert_recursive(self.root, key)
        
    def _insert_recursive(self, root, key):
        """Helper method for insert"""
        if root is None:
            return Node(key)
            
        if key < root.key:
            root.left = self._insert_recursive(root.left, key)
        else:
            root.right = self._insert_recursive(root.right, key)
            
        return root
        
    def search(self, key):
        """Search for a key in the BST"""
        return self._search_recursive(self.root, key)
        
    def _search_recursive(self, root, key):
        """Helper method for search"""
        if root is None or root.key == key:
            return root
            
        if key < root.key:
            return self._search_recursive(root.left, key)
        return self._search_recursive(root.right, key)
        
    def delete(self, key):
        """Delete a key from the BST"""
        self.root = self._delete_recursive(self.root, key)
        
    def _delete_recursive(self, root, key):
        """Helper method for delete"""
        if root is None:
            return root
            
        if key < root.key:
            root.left = self._delete_recursive(root.left, key)
        elif key > root.key:
            root.right = self._delete_recursive(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
                
            # Node with two children
            # Get inorder successor (smallest in right subtree)
            temp = self._min_value_node(root.right)
            root.key = temp.key
            root.right = self._delete_recursive(root.right, temp.key)
            
        return root
        
    def _min_value_node(self, node):
        """Find the node with minimum key value in BST"""
        current = node
        while current.left:
            current = current.left
        return current
        
    def inorder(self):
        """Inorder traversal of BST"""
        result = []
        self._inorder_recursive(self.root, result)
        return result
        
    def _inorder_recursive(self, root, result):
        """Helper method for inorder traversal"""
        if root:
            self._inorder_recursive(root.left, result)
            result.append(root.key)
            self._inorder_recursive(root.right, result)

# Test implementation
if __name__ == "__main__":
    bst = BinarySearchTree()
    keys = [50, 30, 70, 20, 40, 60, 80]
    
    print("Inserting keys:", keys)
    for key in keys:
        bst.insert(key)
    
    print("Inorder traversal:", bst.inorder())
    
    search_key = 40
    print(f"\nSearching for {search_key}:", 
          "Found" if bst.search(search_key) else "Not found")
    
    delete_key = 30
    print(f"\nDeleting {delete_key}")
    bst.delete(delete_key)
    print("Inorder traversal after deletion:", bst.inorder()) 