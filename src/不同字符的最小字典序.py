# 给出一个由a-z组成的字符串S，求他的一个子序列，满足如下条件：

# 1、包含字符串中所有出现过的字符各1个。
# 2、是所有满足条件1的串中，字典序最小的。

# 例如：babbdcc，出现过的字符为：abcd，而包含abcd的所有子序列中，字典序最小的为abdc。

# 解题思路：
#     1、我们创建一个栈，用来存放解。

#     对于这个字符串，我们从第一个字符开始扫：

#     ①如果这个栈此时为空，那么将这个字符丢进去。

#     ②如果栈此时不为空，而且当前这个字符已经在栈中，跳过。

#     ③如果栈此时不为空，而且当前这个字符不在栈中，我们分两种情况讨论：1.如果这个字符比栈顶大，那么直接丢到栈顶即可。2.如果这个比栈顶小，那么我们判断此时栈顶在这个字符后边还是否存在。如果后边还有，那么对应将栈顶弹出，直到不能弹出为止，再将这个字符丢到栈顶。

#     这样我们就能做到尽可能的贪心。


def func(strings):
    n = len(strings)
    stack = []
    i = 0
    while i < n:
        cur_str = strings[i]
        if cur_str in stack:
            i += 1
            continue
        while stack and stack[-1] > cur_str:
            while stack[-1] in strings[i+1:]:
                stack.pop()
            else:
                break
        stack.append(cur_str)
        i += 1

    return stack