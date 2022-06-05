class Solution:
    "输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序"

    # 例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
    # 但4,3,5,1,2就不可能是该压栈序列的弹出序列。
    # 解题思路：使用辅助栈
    # step 1：准备一个辅助栈，两个下标分别访问两个序列。
    # step 2：辅助栈为空或者栈顶不等于出栈数组当前元素，就持续将入栈数组加入栈中。
    # step 3：栈顶等于出栈数组当前元素就出栈。
    # step 4：当入栈数组访问完，出栈数组无法依次弹出，就是不匹配的，否则两个序列都访问完就是匹配的。

    def __init__(self):
        self.stack = []

    def is_pop_order(self, push_array, pop_array):

        if not push_array and not pop_array:
            return True

        if len(push_array) != len(pop_array):
            return False

        j = 0

        for i in range(len(pop_array)):

            while j < len(push_array) and (not self.stack or self.stack[-1] != pop_array[i]):
                self.stack.append(push_array[j])
                j += 1

            if self.stack[-1] == pop_array[i]:
                self.stack.pop()

            else:
                return False

        return True
