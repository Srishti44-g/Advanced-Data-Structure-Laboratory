class InfixToPostfix:
    def __init__(self):
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        self.stack = []
        
    def convert(self, expression):
        """Convert infix expression to postfix"""
        output = []
        
        for char in expression:
            if char.isalnum():  # Operand
                output.append(char)
            elif char == '(':  # Left parenthesis
                self.stack.append(char)
            elif char == ')':  # Right parenthesis
                while self.stack and self.stack[-1] != '(':
                    output.append(self.stack.pop())
                if self.stack and self.stack[-1] == '(':
                    self.stack.pop()
            else:  # Operator
                while (self.stack and self.stack[-1] != '(' and 
                       self.precedence.get(char, 0) <= self.precedence.get(self.stack[-1], 0)):
                    output.append(self.stack.pop())
                self.stack.append(char)
        
        # Pop remaining operators
        while self.stack:
            output.append(self.stack.pop())
            
        return ''.join(output)

# Test implementation
if __name__ == "__main__":
    converter = InfixToPostfix()
    expressions = [
        "a+b*c",
        "(a+b)*c",
        "a+b*c+d",
        "a*(b+c)"
    ]
    
    for expr in expressions:
        print(f"Infix: {expr}")
        print(f"Postfix: {converter.convert(expr)}\n") 