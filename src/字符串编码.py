# 给定一个经过编码的字符串，返回它解码后的字符串。

# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

# 输入：s = "3[a]2[bc]"
# 输出："aaabcbc"

# 解题思路
    # 辅助栈
    # 当 字符为 [ 时，数据入栈，当字符为 ] 时，数据出栈


def func(s):
    stack = []
    multiple = 0
    res = ""

    for i in s:
        if "0" < i < "9":
            multiple = multiple * 10 + int(i)
        elif i == '[':
            stack.append([res,multiple])
            res = ''
            multiple = 0
        elif i == ']':
            pre_res, cur_multiple = stack.pop()
            res = pre_res + cur_multiple * res
        else:
            res += i
    return res

print(func("3[a]2[bc]"))