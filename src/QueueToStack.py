
class QTS:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self,value):
        self.queue1.append(value)

    def pop(self):

        if not self.queue1:
            return None

        while len(self.queue1) != 1:
            self.queue2.append(self.queue1.pop(0))

        self.queue2,self.queue1 = self.queue1,self.queue2

        return self.queue2.pop()