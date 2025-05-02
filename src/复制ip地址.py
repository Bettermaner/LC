
# 给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能从 s 获得的 有效 IP 地址 。你可以按任何顺序返回答案。

# 有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

# 例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。



# 🧠 解题思路：回溯法（Backtracking）
# 这个问题非常适合使用 回溯法 来解决。我们尝试在字符串中插入 3 个点，将字符串划分为 4 段，每段必须满足以下条件：

# ✅ 有效 IP 段的判断规则：
# 长度为 1~3 位；
# 数值范围为 0~255；
# 不能有前导零，除非该段就是 '0' 本身。

# 所以总体时间复杂度是 O(1)（因为划分方式数量固定、有限）。

def restoreIpAddresses(s: str):
    def is_valid(segment: str) -> bool:
        # 长度大于1时不能以0开头
        if len(segment) > 1 and segment[0] == '0':
            return False
        # 数值必须在0~255之间
        return 0 <= int(segment) <= 255

    def backtrack(start: int, path: list):
        # 如果已经选了4段，并且走到了字符串末尾，则是一个有效IP
        if len(path) == 4:
            if start == len(s):
                result.append(".".join(path))
            return

        # 尝试截取1~3个字符作为当前段
        for length in range(1, 4):
            end = start + length
            if end > len(s):
                break
            segment = s[start:end]
            if is_valid(segment):
                backtrack(end, path + [segment])

    result = []
    backtrack(0, [])
    return result