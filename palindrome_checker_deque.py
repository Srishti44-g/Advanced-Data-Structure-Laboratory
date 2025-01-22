from collections import deque

def is_palindrome(s):
    """
    Check if the given string is a palindrome using a stack and a queue.

    Args:
        s (str): The input string.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Normalize the string: remove non-alphanumeric characters and convert to lowercase
    s = ''.join(char.lower() for char in s if char.isalnum())

    # Initialize a stack and a queue
    stack = []
    queue = deque()

    # Populate the stack and the queue with characters from the string
    for char in s:
        stack.append(char)
        queue.append(char)

    # Compare characters popped from the stack and dequeued from the queue
    while stack:
        if stack.pop() != queue.popleft():
            return False

    return True

# Test the function
if __name__ == "__main__":
    test_string = input("Enter a string to check if it is a palindrome: ")
    if is_palindrome(test_string):
        print(f"\"{test_string}\" is a palindrome.")
    else:
        print(f"\"{test_string}\" is not a palindrome.")
