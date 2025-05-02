# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

# 注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。

#  示例 1:

# 输入: num1 = "2", num2 = "3"
# 输出: "6"
# 示例 2:

# 输入: num1 = "123", num2 = "456"
# 输出: "56088"

# 解题思路：
# 举个例子：
# 我们不需要真正构造每一行相乘的结果，而是可以使用一个数组来记录每一位的累加结果。
# 1 2 3
#     × 4 5 6
#     ---------
#       7 3 8   ← 123 × 6
#     6 1 5     ← 123 × 5（注意进位和错位）
#   4 9 2       ← 123 × 4（再错一位）
#   -------------
#   结果：5 6 0 8 8


# ✅ 总体时间复杂度：O(m × n)
# ✅ 空间复杂度：O(m + n)

# 模拟每一位相乘，并把结果加到 result 数组中相应位置
# p1 和 p2 是当前乘积应该放到哪两个位置上（因为最多两位）
# 处理进位（十位加到 p1，个位留在 p2）

def multiply(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"

    m, n = len(num1), len(num2)
    # 最多有 m + n 位（比如 999×999=999001，是 6 位）
    # result[i] 表示第 i 位的值（未进位）
    result = [0] * (m + n)

    # 从后往前遍历 num1 和 num2
    for i in range(m - 1, -1, -1):
        digit1 = int(num1[i])
        for j in range(n - 1, -1, -1):
            digit2 = int(num2[j])
            product = digit1 * digit2

            # 乘积的两个位置索引
            # p1 和 p2 是当前乘积应该放到哪两个位置上（因为最多两位）
            p1 = i + j
            p2 = i + j + 1

            # 累加到对应的位置
            result[p2] += product
            result[p1] += result[p2] // 10  # 进位处理
            result[p2] %= 10  # 当前位只保留个位数

    # 因为提前都填0了，所以需要将首位为0的字符去掉
    while result[0] == 0:
        result.pop(0)

    return ''.join(map(str, result)) or "0"