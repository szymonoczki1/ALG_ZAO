class Stack:
    def __init__(self) -> None:
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if not self.stack:
            return "Error, cant pop from empty stack."

        return self.stack.pop()
    
    def peek(self):
        if not self.stack:
            return "Error, cant peek into an empty stack."
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0