# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和并同样以字符串形式返回。

# 你不能使用任何內建的用于处理大整数的库（比如 BigInteger）， 也不能直接将输入的字符串转换为整数形式。

# 示例 1：

# 输入：num1 = "11", num2 = "123"
# 输出："134"
# 示例 2：

# 输入：num1 = "456", num2 = "77"
# 输出："533"
#示例 3：

# 输入：num1 = "0", num2 = "0"
# 输出："0"
 


# 解题思路：这个问题的核心在于模拟手算加法的过程，从右往左逐位相加，并处理进位（carry）。

# 步骤如下：
# 使用两个指针 i 和 j，分别指向 num1 和 num2 的末尾。
# 循环直到两个字符串都处理完且没有进位为止。
# 每次取当前位的数字（如果已处理完则为 0），加上进位值。
# 当前位的结果为 sum % 10，进位为 sum // 10。
# 将每一位结果添加到结果列表中。
# 最终反转结果列表，得到正确顺序的字符串。

# 时间复杂度：O(max(len(num1), len(num2)))，每个字符最多处理一次。
# 空间复杂度：O(max(len(num1), len(num2)))，用于存储结果字符串。


def addStrings(num1: str, num2: str) -> str:
    i = len(num1) - 1
    j = len(num2) - 1
    carry = 0
    result = []

    while i >= 0 or j >= 0 or carry:
        # 获取当前位的数字（如果是有效位置）否则为 0
        digit1 = int(num1[i]) if i >= 0 else 0
        digit2 = int(num2[j]) if j >= 0 else 0

        # 计算当前位总和与进位
        total = digit1 + digit2 + carry
        carry = total // 10
        result.append(str(total % 10))

        # 移动指针
        i -= 1
        j -= 1

    # 因为我们是从低位开始计算的，所以要反转结果
    return ''.join(result[::-1])

# 示例测试
num1 = "123"
num2 = "456"
print(addStrings(num1, num2))  # 输出: "579"

num1 = "999"
num2 = "9999"
print(addStrings(num1, num2))  # 输出: "10998"