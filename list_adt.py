class ArrayList:
    """Implementation of List ADT using array (Python list)"""
    
    def __init__(self):
        self.array = []
        
    def append(self, item):
        """Add an item to the end of the list"""
        self.array.append(item)
        
    def insert(self, index, item):
        """Insert an item at a specific index"""
        self.array.insert(index, item)
        
    def remove(self, item):
        """Remove first occurrence of item"""
        try:
            self.array.remove(item)
            return True
        except ValueError:
            return False
            
    def pop(self, index=-1):
        """Remove and return item at index (default last)"""
        return self.array.pop(index)
        
    def get(self, index):
        """Get item at index"""
        return self.array[index]
        
    def size(self):
        """Return number of items in list"""
        return len(self.array)
        
    def is_empty(self):
        """Check if list is empty"""
        return len(self.array) == 0
        
    def __str__(self):
        return str(self.array)

class Node:
    """Node class for LinkedList"""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Implementation of List ADT using linked list"""
    
    def __init__(self):
        self.head = None
        self._size = 0
        
    def append(self, item):
        """Add an item to the end of the list"""
        new_node = Node(item)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self._size += 1
        
    def insert(self, index, item):
        """Insert an item at a specific index"""
        if index < 0 or index > self._size:
            raise IndexError("Index out of range")
            
        new_node = Node(item)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self._size += 1
        
    def remove(self, item):
        """Remove first occurrence of item"""
        if not self.head:
            return False
            
        if self.head.data == item:
            self.head = self.head.next
            self._size -= 1
            return True
            
        current = self.head
        while current.next:
            if current.next.data == item:
                current.next = current.next.next
                self._size -= 1
                return True
            current = current.next
        return False
        
    def size(self):
        """Return number of items in list"""
        return self._size
        
    def is_empty(self):
        """Check if list is empty"""
        return self._size == 0
        
    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(str(current.data))
            current = current.next
        return "[" + ", ".join(result) + "]"

# Test the implementations
if __name__ == "__main__":
    # Test ArrayList
    print("Testing ArrayList:")
    arr_list = ArrayList()
    arr_list.append(1)
    arr_list.append(2)
    arr_list.append(3)
    print("After appending 1, 2, 3:", arr_list)
    
    arr_list.insert(1, 4)
    print("After inserting 4 at index 1:", arr_list)
    
    arr_list.remove(2)
    print("After removing 2:", arr_list)
    
    # Test LinkedList
    print("\nTesting LinkedList:")
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    print("After appending 1, 2, 3:", linked_list)
    
    linked_list.insert(1, 4)
    print("After inserting 4 at index 1:", linked_list)
    
    linked_list.remove(2)
    print("After removing 2:", linked_list) 