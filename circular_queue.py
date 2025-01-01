class CircularQueue:
    """Implementation of Circular Queue ADT using array"""
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1
        
    def is_full(self):
        """Check if queue is full"""
        return ((self.rear + 1) % self.capacity == self.front or
                (self.front == 0 and self.rear == self.capacity - 1))
        
    def is_empty(self):
        """Check if queue is empty"""
        return self.front == -1
        
    def enqueue(self, item):
        """Add an item to the queue"""
        if self.is_full():
            raise IndexError("Queue is full")
            
        if self.front == -1:  # First element
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity
            
        self.queue[self.rear] = item
        
    def dequeue(self):
        """Remove and return the front item"""
        if self.is_empty():
            raise IndexError("Queue is empty")
            
        item = self.queue[self.front]
        
        if self.front == self.rear:  # Last element
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
            
        return item
        
    def __str__(self):
        if self.is_empty():
            return "[]"
            
        items = []
        index = self.front
        while True:
            items.append(str(self.queue[index]))
            if index == self.rear:
                break
            index = (index + 1) % self.capacity
        return "[" + ", ".join(items) + "]"

# Test implementation
if __name__ == "__main__":
    cq = CircularQueue(5)
    print("Enqueuing: 1, 2, 3, 4")
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    cq.enqueue(4)
    print("Queue:", cq)
    
    print("\nDequeuing two items")
    print("Dequeued:", cq.dequeue())
    print("Dequeued:", cq.dequeue())
    print("Queue:", cq)
    
    print("\nEnqueuing: 5, 6")
    cq.enqueue(5)
    cq.enqueue(6)
    print("Queue:", cq) 