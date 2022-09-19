


class solution():
    "将字符串转化成数值"
    # 1.去掉无用的前导空格
    # 2.第一个非空字符为+或者-号时，作为该整数的正负号，如果没有符号，默认为正数
    # 3.判断整数的有效部分：
        # 3.1 确定符号位之后，与之后面尽可能多的连续数字组合起来成为有效整数数字，如果没有有效的整数部分，那么直接返回0
        # 3.2 将字符串前面的整数部分取出，后面可能会存在存在多余的字符(字母，符号，空格等)，这些字符可以被忽略，它们对于函数不应该造成影响
        # 3.3  整数超过 32 位有符号整数范围 [−231,  231 − 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −231的整数应该被调整为 −231 ，大于 231 − 1 的整数应该被调整为 231 − 1
    # 4.去掉无用的后导空格
    def __init__(self) -> None:
        self.index = 0

    def str_to_int(self,string):
        # 解题思路: 遍历

        if not len(string):
            return 0

        # 先去除空格
        s = string.strip()

        l = len(s)

        # 判断是否是一个空串
        if not l:
            return 0

        # 如果没有正负号，默认是正
        sign = 1
        if s[self.index] == "+":
            self.index += 1

        elif s[self.index] == "-":
            self.index += 1
            sign = -1

        # 判断是否只含有正负号
        if self.index == l:
            return 0

        # 判断数字是否在里面
        res = 0
        while self.index < l:
            num = s[self.index]
            if num < "0" or num > "9":
                break
            res =  res * 10 + sign * int(num)
            self.index += 1

        # 判断数字大小是否在边界
        if res >= 2 ** 31:
            res = 2 ** 31 -1
        elif res <=  -2 ** 31:
            res =  -2 ** 31
        return res

        
