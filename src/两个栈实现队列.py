
# 总结
# push 操作：O(1)
# pop 操作：最坏情况下 O(n)，但摊销后为 O(1)

class STQ:
    "两个栈实现队列"
    
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self,value):
        self.stack1.append(value)

    def pop(self):
        # 首先从stack2里面拿
        if self.stack2:
            return self.stack2.pop()

        if not self.stack1:
            return None
        # 然后始终从stack1里面拿，全部放在stack2里面
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        return self.stack2.pop()