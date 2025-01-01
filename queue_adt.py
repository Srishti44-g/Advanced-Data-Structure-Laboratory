class ArrayQueue:
    """Implementation of Queue ADT using array (Python list)"""
    
    def __init__(self):
        self.items = []
        
    def enqueue(self, item):
        """Add an item to the rear of the queue"""
        self.items.append(item)
        
    def dequeue(self):
        """Remove and return the front item"""
        if not self.is_empty():
            return self.items.pop(0)
        raise IndexError("Queue is empty")
        
    def front(self):
        """Return the front item without removing it"""
        if not self.is_empty():
            return self.items[0]
        raise IndexError("Queue is empty")
        
    def is_empty(self):
        """Check if queue is empty"""
        return len(self.items) == 0
        
    def size(self):
        """Return number of items in queue"""
        return len(self.items)
        
    def __str__(self):
        return str(self.items)

# Test implementation
if __name__ == "__main__":
    queue = ArrayQueue()
    print("Enqueuing items: 1, 2, 3")
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("Queue:", queue)
    print("Dequeue:", queue.dequeue())
    print("Front:", queue.front())
    print("Queue after operations:", queue) 