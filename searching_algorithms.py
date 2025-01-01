def linear_search_iterative(arr, target):
    """
    Iterative implementation of linear search
    
    Args:
        arr (list): List to search in
        target: Element to find
        
    Returns:
        int: Index of target if found, -1 if not found
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def linear_search_recursive(arr, target, index=0):
    """
    Recursive implementation of linear search
    
    Args:
        arr (list): List to search in
        target: Element to find
        index (int): Current index being checked
        
    Returns:
        int: Index of target if found, -1 if not found
    """
    # Base cases
    if index >= len(arr):
        return -1
    if arr[index] == target:
        return index
    
    # Recursive case
    return linear_search_recursive(arr, target, index + 1)

def binary_search_iterative(arr, target):
    """
    Iterative implementation of binary search
    
    Args:
        arr (list): Sorted list to search in
        target: Element to find
        
    Returns:
        int: Index of target if found, -1 if not found
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def binary_search_recursive(arr, target, left=0, right=None):
    """
    Recursive implementation of binary search
    
    Args:
        arr (list): Sorted list to search in
        target: Element to find
        left (int): Left boundary of current search
        right (int): Right boundary of current search
        
    Returns:
        int: Index of target if found, -1 if not found
    """
    if right is None:
        right = len(arr) - 1
        
    if left > right:
        return -1
        
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# Test the implementations
if __name__ == "__main__":
    # Test array
    test_array = [1, 3, 5, 7, 9, 11, 13, 15, 17]
    target = 7
    
    print("Test Array:", test_array)
    print("Searching for:", target)
    print("\nLinear Search Results:")
    print("Iterative:", linear_search_iterative(test_array, target))
    print("Recursive:", linear_search_recursive(test_array, target))
    
    print("\nBinary Search Results:")
    print("Iterative:", binary_search_iterative(test_array, target))
    print("Recursive:", binary_search_recursive(test_array, target)) 