class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    """Binary Tree with different traversal methods"""
    
    def __init__(self):
        self.root = None
        
    def preorder_recursive(self, root, result=None):
        """Recursive preorder traversal"""
        if result is None:
            result = []
            
        if root:
            result.append(root.key)
            self.preorder_recursive(root.left, result)
            self.preorder_recursive(root.right, result)
            
        return result
        
    def preorder_iterative(self, root):
        """Iterative preorder traversal"""
        if not root:
            return []
            
        result = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            result.append(node.key)
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
        return result
        
    def inorder_recursive(self, root, result=None):
        """Recursive inorder traversal"""
        if result is None:
            result = []
            
        if root:
            self.inorder_recursive(root.left, result)
            result.append(root.key)
            self.inorder_recursive(root.right, result)
            
        return result
        
    def inorder_iterative(self, root):
        """Iterative inorder traversal"""
        result = []
        stack = []
        current = root
        
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
                
            current = stack.pop()
            result.append(current.key)
            current = current.right
            
        return result
        
    def postorder_recursive(self, root, result=None):
        """Recursive postorder traversal"""
        if result is None:
            result = []
            
        if root:
            self.postorder_recursive(root.left, result)
            self.postorder_recursive(root.right, result)
            result.append(root.key)
            
        return result
        
    def postorder_iterative(self, root):
        """Iterative postorder traversal"""
        if not root:
            return []
            
        result = []
        stack1 = [root]
        stack2 = []
        
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
                
        while stack2:
            node = stack2.pop()
            result.append(node.key)
            
        return result

# Test implementation
if __name__ == "__main__":
    # Create a binary tree
    tree = BinaryTree()
    tree.root = TreeNode(1)
    tree.root.left = TreeNode(2)
    tree.root.right = TreeNode(3)
    tree.root.left.left = TreeNode(4)
    tree.root.left.right = TreeNode(5)
    
    print("Tree Traversals:")
    print("\nPreorder:")
    print("Recursive:", tree.preorder_recursive(tree.root))
    print("Iterative:", tree.preorder_iterative(tree.root))
    
    print("\nInorder:")
    print("Recursive:", tree.inorder_recursive(tree.root))
    print("Iterative:", tree.inorder_iterative(tree.root))
    
    print("\nPostorder:")
    print("Recursive:", tree.postorder_recursive(tree.root))
    print("Iterative:", tree.postorder_iterative(tree.root)) 