class ArrayStack:
    """Implementation of Stack ADT using array (Python list)"""
    
    def __init__(self):
        self.items = []
        
    def push(self, item):
        """Push an item onto the stack"""
        self.items.append(item)
        
    def pop(self):
        """Remove and return the top item"""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Stack is empty")
        
    def peek(self):
        """Return the top item without removing it"""
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Stack is empty")
        
    def is_empty(self):
        """Check if stack is empty"""
        return len(self.items) == 0
        
    def size(self):
        """Return number of items in stack"""
        return len(self.items)
        
    def __str__(self):
        return str(self.items)

# Test implementation
if __name__ == "__main__":
    stack = ArrayStack()
    print("Pushing items: 1, 2, 3")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Stack:", stack)
    print("Pop:", stack.pop())
    print("Peek:", stack.peek())
    print("Stack after operations:", stack) 