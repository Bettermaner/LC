class solution:
    "定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的 min 函数，输入操作时保证 pop、top 和 min 函数操作时，栈中一定有元素。"

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.stack_min = []

    def push(self, node: int) -> None:
        self.stack.append(node)
        if not self.stack_min or node <= self.stack_min[-1]:
            self.stack_min.append(node)
        else:
            self.stack_min.append(self.stack_min[-1])

    def pop(self) -> None:
        val = self.stack.pop()
        self.stack_min.pop()
        return val

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_min[-1]
