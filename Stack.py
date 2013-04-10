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
        last = self.content[-1]
        self.content = self.content[0:-1]
        return last

    def top(self):
        return self.content[-1]
