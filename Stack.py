
class Stack:
    def __init__(self):
        self.stack = []

    def  is_empty(self):
        if self.size() == 0:
            return False
        return True

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        removed = self.stack.pop()
        return removed

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)
