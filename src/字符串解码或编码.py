# 给定一个经过编码的字符串，返回它解码后的字符串。

# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

# 输入：s = "3[a]2[bc]"
# 输出："aaabcbc"

# 🧠 解题思路
# 我们可以使用 栈（stack） 来处理嵌套结构的括号。具体来说：

# 遇到数字时，我们要把完整的数字拼起来（因为可能有 10 或更大的数）；
# 遇到 [ 时，把当前的字符串和数字压入栈中；
# 遇到 ] 时，弹出栈中的数字和之前的字符串，进行重复操作；
# 使用一个临时变量保存当前构建的字符串。


# 时间复杂度: O(n)，其中 n 是字符串长度。
# 每个字符最多被处理一次（进栈/出栈或拼接），虽然某些字符会被多次拼接到字符串中，但总的操作次数仍然是线性的。
# 空间复杂度: O(n)
# 最坏情况下，所有字符都嵌套在括号内，需要栈存储中间结果。


def decodeString(s: str) -> str:
    stack = []
    current_num = 0
    current_str = ''

    for char in s:
        if char.isdigit():
            # 构建多位数字
            current_num = current_num * 10 + int(char)

        elif char == '[':
            # 将当前字符串和数字压栈
            stack.append((current_str, current_num))
            current_str = ''
            current_num = 0

        elif char == ']':
            # 弹出栈顶的字符串和数字
            prev_str, repeat_time = stack.pop()
            current_str = prev_str + current_str * repeat_time

        else:
            # 普通字符直接加到当前字符串中
            current_str += char

    return current_str