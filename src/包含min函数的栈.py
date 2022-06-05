class solution:
    "定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的 min 函数，输入操作时保证 pop、top 和 min 函数操作时，栈中一定有元素。"

    def __init__(self):
        self.stack = []
        self.stack_min = []

    def push(self, node):
        self.stack.append(node)
        if not self.stack_min:
            self.stack_min.append(node)

        # 最小栈的位置 始终记录栈对应的长度下的最小值。
        if node > self.stack_min[-1]:
            self.stack_min.append(self.stack_min[-1])
        else:
            self.stack_min.append(node)

    def top(self):
        return self.stack[-1]

    def pop(self):
        val = self.stack.pop()
        self.stack_min.pop()
        return val

    def min(self):
        return self.stack_min[-1]
