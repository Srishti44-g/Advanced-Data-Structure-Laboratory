from stack_adt import ArrayStack
from queue_adt import ArrayQueue

class PalindromeChecker:
    """Check if a string is palindrome using stack and queue"""
    
    def __init__(self):
        self.stack = ArrayStack()
        self.queue = ArrayQueue()
        
    def is_palindrome(self, text):
        """
        Check if text is palindrome
        
        Args:
            text (str): Text to check
            
        Returns:
            bool: True if text is palindrome, False otherwise
        """
        # Clean the text - remove spaces and convert to lowercase
        text = ''.join(c.lower() for c in text if c.isalnum())
        
        # Push characters to stack and queue
        for char in text:
            self.stack.push(char)
            self.queue.enqueue(char)
            
        # Compare characters from stack and queue
        while not self.stack.is_empty():
            if self.stack.pop() != self.queue.dequeue():
                return False
        return True

# Test implementation
if __name__ == "__main__":
    checker = PalindromeChecker()
    test_strings = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "Was it a car or a cat I saw?",
        "hello",
        "Madam, I'm Adam"
    ]
    
    for text in test_strings:
        result = checker.is_palindrome(text)
        print(f"'{text}' is{' ' if result else ' not '}a palindrome") 