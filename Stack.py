class Stack():
    def __init__(self):
        self.content = []

    def isEmpty(self):
        if len(self.content) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.content)

    def push(self, num):
        self.content.append(num)

    def pop(self):
        try:
            last = self.content[-1]
            self.content = self.content[0:-1]
            return last
        except:
            raise EmptyStackException()

    def top(self):
        try:
            return self.content[-1]
        except:
            raise EmptyStackException()

class EmptyStackException(Exception):
    def __repr__(self):
        return "The stack is empty."
