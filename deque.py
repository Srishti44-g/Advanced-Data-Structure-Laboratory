class ArrayDeque:
    """Implementation of Deque ADT using array"""
    
    def __init__(self):
        self.items = []
        
    def add_front(self, item):
        """Add an item to the front"""
        self.items.insert(0, item)
        
    def add_rear(self, item):
        """Add an item to the rear"""
        self.items.append(item)
        
    def remove_front(self):
        """Remove and return the front item"""
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("Deque is empty")
        
    def remove_rear(self):
        """Remove and return the rear item"""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Deque is empty")
        
    def front(self):
        """Return the front item"""
        if not self.is_empty():
            return self.items[0]
        raise IndexError("Deque is empty")
        
    def rear(self):
        """Return the rear item"""
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Deque is empty")
        
    def is_empty(self):
        """Check if deque is empty"""
        return len(self.items) == 0
        
    def size(self):
        """Return number of items in deque"""
        return len(self.items)
        
    def __str__(self):
        return str(self.items)

# Test implementation
if __name__ == "__main__":
    deque = ArrayDeque()
    print("Adding items to front: 1, 2")
    deque.add_front(1)
    deque.add_front(2)
    print("Adding items to rear: 3, 4")
    deque.add_rear(3)
    deque.add_rear(4)
    print("Deque:", deque)
    
    print("\nRemoving from front:", deque.remove_front())
    print("Removing from rear:", deque.remove_rear())
    print("Deque after operations:", deque) 