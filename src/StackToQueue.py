


class STQ:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self,value):
        self.stack1.append(value)

    def pop(self):

        if self.stack2:
            return self.stack2.pop()

        if not self.stack1:
            return None

        while self.stack1:
            self.stack2.append(self.stack1.pop())

        return self.stack2.pop()