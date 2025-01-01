# Advanced Data Structures Laboratory 🚀

A comprehensive collection of Data Structures and Algorithms implementations in Python. This repository contains well-documented code for various data structure operations and algorithms.

## 📚 Table of Contents

### 1. Searching Algorithms
Implementation of fundamental searching techniques with both iterative and recursive approaches.
- [Linear Search](experiments/01_searching/searching_algorithms.py)
  - Iterative implementation
  - Recursive implementation
- [Binary Search](experiments/01_searching/searching_algorithms.py)
  - Iterative implementation
  - Recursive implementation
- Time Complexity: - O(n) for Linear Search
                   - O(log n) for Binary Search

### 2. List ADT Implementation
Different implementations of List Abstract Data Type.
- [Array-based List](experiments/02_list_adt/list_adt.py)
  - Dynamic array implementation
  - Basic operations (append, insert, remove)
- [Linked List](experiments/02_list_adt/list_adt.py)
  - Singly linked list implementation
  - Node-based structure
  - Basic operations

### 3. Stack ADT Implementation
Stack data structure with array-based implementation.
- [Stack Operations](experiments/03_stack/stack_adt.py)
  - Push operation
  - Pop operation
  - Peek operation
  - isEmpty check
  - Size tracking

### 4. Queue ADT Implementation
Queue data structure with array-based implementation.
- [Queue Operations](experiments/04_queue/queue_adt.py)
  - Enqueue operation
  - Dequeue operation
  - Front element access
  - Basic queue utilities

### 5. Infix to Postfix Conversion
Expression conversion using stack data structure.
- [Expression Converter](experiments/05_infix_postfix/infix_to_postfix.py)
  - Operator precedence handling
  - Stack-based conversion
  - Expression evaluation

### 6. Circular Queue Implementation
Advanced queue implementation with circular array structure.
- [Circular Queue](experiments/06_circular_queue/circular_queue.py)
  - Efficient space utilization
  - Circular array operations
  - Full/Empty state handling

## 🛠️ Setup and Installation

### Prerequisites
- Python 3.x
- Git (for cloning the repository)

### Running the Programs

1. Clone the repository:
   git clone[ https://github.com/yourusername/advanced-data-structures-lab.git](https://github.com/Srishti44-g/Advanced-Data-Structure-Laboratroy)
   cd advanced-data-structures-lab
2. Navigate to specific experiment directory:
   cd experiments/01_searching
3. Run the Python file:
   python searching_algorithms.py



## 📝 Documentation

Each implementation includes:
- Detailed comments explaining the algorithm
- Time and space complexity analysis
- Example usage in the main section
- Test cases demonstrating functionality

## 🧪 Testing

Each module contains a test section in the `if __name__ == "__main__":` block. Run the files directly to see the test outputs.

Example output for Searching Algorithms:
python
- Test Array: [1, 3, 5, 7, 9, 11, 13, 15, 17]
- Searching for: 7
#### Linear Search Results:
- Iterative: 3
- Recursive: 3
#### Binary Search Results:
- Iterative: 3
- Recursive: 3

## 📊 Time Complexity Analysis

| Algorithm/Operation | Average Case | Worst Case | Space Complexity |
|-------------------|--------------|------------|------------------|
| Linear Search     | O(n)         | O(n)       | O(1)            |
| Binary Search     | O(log n)     | O(log n)   | O(1)            |
| Stack Operations  | O(1)         | O(1)       | O(n)            |
| Queue Operations  | O(1)         | O(1)       | O(n)            |
| Circular Queue    | O(1)         | O(1)       | O(n)            |
| List Operations   | O(1)/O(n)    | O(n)       | O(n)            |

# Data Structures Time & Space Complexity

## 📊 Array/List Operations
| Operation               | Average Case | Worst Case | Space Complexity |
|------------------------|--------------|------------|------------------|
| Access                 | O(1)         | O(1)       | O(1)            |
| Search                 | O(n)         | O(n)       | O(1)            |
| Binary Search (sorted) | O(log n)     | O(log n)   | O(1)            |
| Insertion (at end)     | O(1)         | O(1)       | O(1)            |
| Insertion (at start)   | O(n)         | O(n)       | O(1)            |
| Deletion (at end)      | O(1)         | O(1)       | O(1)            |
| Deletion (at start)    | O(n)         | O(n)       | O(1)            |

## 📚 Stack & Queue Operations
| Operation               | Average Case | Worst Case | Space Complexity |
|------------------------|--------------|------------|------------------|
| Stack Push             | O(1)         | O(1)       | O(1)            |
| Stack Pop              | O(1)         | O(1)       | O(1)            |
| Stack Peek             | O(1)         | O(1)       | O(1)            |
| Queue Enqueue          | O(1)         | O(1)       | O(1)            |
| Queue Dequeue          | O(1)         | O(1)       | O(1)            |
| Queue Peek             | O(1)         | O(1)       | O(1)            |
| Circular Queue All Ops | O(1)         | O(1)       | O(1)            |

## 🔗 Linked List Operations
| Operation               | Average Case | Worst Case | Space Complexity |
|------------------------|--------------|------------|------------------|
| Access                 | O(n)         | O(n)       | O(1)            |
| Search                 | O(n)         | O(n)       | O(1)            |
| Insertion (at start)   | O(1)         | O(1)       | O(1)            |
| Insertion (at end)*    | O(1)         | O(1)       | O(1)            |
| Insertion (at middle)  | O(n)         | O(n)       | O(1)            |
| Deletion (at start)    | O(1)         | O(1)       | O(1)            |
| Deletion (at end)      | O(n)         | O(n)       | O(1)            |
| Deletion (at middle)   | O(n)         | O(n)       | O(1)            |

## 🗺️ Hash Table Operations
| Operation               | Average Case | Worst Case | Space Complexity |
|------------------------|--------------|------------|------------------|
| Insertion              | O(1)         | O(n)       | O(n)            |
| Deletion               | O(1)         | O(n)       | O(1)            |
| Search                 | O(1)         | O(n)       | O(1)            |
| Access                 | O(1)         | O(n)       | O(1)            |

## 🌳 Binary Search Tree Operations
| Operation               | Average Case | Worst Case | Space Complexity |
|------------------------|--------------|------------|------------------|
| Access                 | O(log n)     | O(n)       | O(1)            |
| Search                 | O(log n)     | O(n)       | O(1)            |
| Insertion              | O(log n)     | O(n)       | O(1)            |
| Deletion               | O(log n)     | O(n)       | O(1)            |

## 🔄 AVL Tree Operations
| Operation               | Average Case | Worst Case | Space Complexity |
|------------------------|--------------|------------|------------------|
| Access                 | O(log n)     | O(log n)   | O(1)            |
| Search                 | O(log n)     | O(log n)   | O(1)            |
| Insertion              | O(log n)     | O(log n)   | O(1)            |
| Deletion               | O(log n)     | O(log n)   | O(1)            |

## 📊 Heap Operations
| Operation               | Average Case | Worst Case | Space Complexity |
|------------------------|--------------|------------|------------------|
| Build Heap             | O(n)         | O(n)       | O(n)            |
| Insert                 | O(log n)     | O(log n)   | O(1)            |
| Delete                 | O(log n)     | O(log n)   | O(1)            |
| Get Min/Max            | O(1)         | O(1)       | O(1)            |
| Heapify                | O(log n)     | O(log n)   | O(1)            |

## 🕸️ Graph Operations (Adjacency List)
| Operation                     | Average Case | Worst Case | Space Complexity |
|------------------------------|--------------|------------|------------------|
| Add Vertex                   | O(1)         | O(1)       | O(1)            |
| Add Edge                     | O(1)         | O(1)       | O(1)            |
| Remove Vertex                | O(V + E)     | O(V + E)   | O(1)            |
| Remove Edge                  | O(E)         | O(E)       | O(1)            |
| DFS                         | O(V + E)     | O(V + E)   | O(V)            |
| BFS                         | O(V + E)     | O(V + E)   | O(V)            |

### Notes:
- V = number of vertices
- E = number of edges
- n = number of elements
- *For Linked List: O(1) insertion at end assumes we maintain a tail pointer
- Worst case for Hash Table operations occurs when there are many collisions
- BST operations' worst case occurs with an unbalanced tree
- Space complexity often refers to extra space needed beyond input storage

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## 🌟 Acknowledgments

- Thanks to all contributors who have helped with the implementations
- Special thanks to the Computer Science department for the guidance
- References to standard algorithms and data structures textbooks

---
⭐️ Star this repository if you find it helpful!
