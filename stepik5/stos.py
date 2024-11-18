class Stack:
    def __init__(self) -> None:
        self.stack = []
        self.first_empty_index = 0
    
    def push(self, element):
        self.stack.append(element)
        self.first_empty_index += 1

    def pop(self):
        if self.first_empty_index == 0:
            return "Error, cant pop from empty stack."
        self.first_empty_index -= 1
        return self.stack[self.first_empty_index]
    
    def peek(self):
        if self.first_empty_index == 0:
            return "Error, cant peek into an empty stack."
        return self.stack[self.first_empty_index-1]
    
    def is_empty(self):
        return self.first_empty_index == 0
