class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    """Implementation of Stack ADT using linked list"""
    
    def __init__(self):
        self.top = None
        self._size = 0
        
    def push(self, item):
        """Push an item onto the stack"""
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1
        
    def pop(self):
        """Remove and return the top item"""
        if self.is_empty():
            raise IndexError("Stack is empty")
            
        item = self.top.data
        self.top = self.top.next
        self._size -= 1
        return item
        
    def peek(self):
        """Return the top item without removing it"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.top.data
        
    def is_empty(self):
        """Check if stack is empty"""
        return self.top is None
        
    def size(self):
        """Return number of items in stack"""
        return self._size
        
    def __str__(self):
        items = []
        current = self.top
        while current:
            items.append(str(current.data))
            current = current.next
        return "[" + ", ".join(items) + "]"

# Test implementation
if __name__ == "__main__":
    stack = LinkedStack()
    print("Pushing items: 1, 2, 3")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Stack:", stack)
    print("Pop:", stack.pop())
    print("Peek:", stack.peek())
    print("Stack after operations:", stack) 