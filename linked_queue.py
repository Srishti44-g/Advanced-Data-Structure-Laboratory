class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    """Implementation of Queue ADT using linked list"""
    
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0
        
    def enqueue(self, item):
        """Add an item to the rear of the queue"""
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self._size += 1
        
    def dequeue(self):
        """Remove and return the front item"""
        if self.is_empty():
            raise IndexError("Queue is empty")
            
        item = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self._size -= 1
        return item
        
    def front_item(self):
        """Return the front item without removing it"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.data
        
    def is_empty(self):
        """Check if queue is empty"""
        return self.front is None
        
    def size(self):
        """Return number of items in queue"""
        return self._size
        
    def __str__(self):
        items = []
        current = self.front
        while current:
            items.append(str(current.data))
            current = current.next
        return "[" + ", ".join(items) + "]"

# Test implementation
if __name__ == "__main__":
    queue = LinkedQueue()
    print("Enqueuing items: 1, 2, 3")
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("Queue:", queue)
    print("Dequeue:", queue.dequeue())
    print("Front:", queue.front_item())
    print("Queue after operations:", queue) 