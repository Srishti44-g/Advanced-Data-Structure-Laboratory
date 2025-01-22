class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Recursive Traversals
def preorder_recursive(root):
    if root:
        print(root.val, end=' ')
        preorder_recursive(root.left)
        preorder_recursive(root.right)

def inorder_recursive(root):
    if root:
        inorder_recursive(root.left)
        print(root.val, end=' ')
        inorder_recursive(root.right)

def postorder_recursive(root):
    if root:
        postorder_recursive(root.left)
        postorder_recursive(root.right)
        print(root.val, end=' ')

# Non-Recursive Traversals
def preorder_non_recursive(root):
    if root is None:
        return
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val, end=' ')
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

def inorder_non_recursive(root):
    stack = []
    current = root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        print(current.val, end=' ')
        current = current.right

def postorder_non_recursive(root):
    if root is None:
        return
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
        print(stack2.pop().val, end=' ')

# Example Binary Tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Recursive Preorder:")
preorder_recursive(root)
print("\nNon-Recursive Preorder:")
preorder_non_recursive(root)

print("\nRecursive Inorder:")
inorder_recursive(root)
print("\nNon-Recursive Inorder:")
inorder_non_recursive(root)

print("\nRecursive Postorder:")
postorder_recursive(root)
print("\nNon-Recursive Postorder:")
postorder_non_recursive(root)
