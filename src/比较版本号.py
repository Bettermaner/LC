# 给你两个 版本号字符串 version1 和 version2 ，请你比较它们。版本号由被点 '.' 分开的修订号组成。修订号的值 是它 转换为整数 并忽略前导零。
# 比较版本号时，请按 从左到右的顺序 依次比较它们的修订号。如果其中一个版本字符串的修订号较少，则将缺失的修订号视为 0。
# 返回规则如下：
# 如果 version1 < version2 返回 -1，
# 如果 version1 > version2 返回 1，
# 除此之外返回 0。

# 输入：version1 = "1.2", version2 = "1.10"
# 输出：-1
# 解释：
# version1 的第二个修订号为 "2"，version2 的第二个修订号为 "10"：2 < 10，所以 version1 < version2。

# 示例 3：
# 输入：version1 = "1.0", version2 = "1.0.0.0"
# 输出：0
# 解释：
# version1 有更少的修订号，每个缺失的修订号按 "0" 处理。


# 🧠 实现思路
# 分割字符串：将版本号字符串按 '.' 分割为多个修订号。
# 逐位比较：从左到右依次比较两个版本号的对应修订号。
# 处理长度差异：如果一个版本号较短，则视为后续修订号为 0。
# 返回结果：一旦发现不同的修订号，立即返回比较结果；若所有修订号都相同，则返回 0 表示版本号相等。

# 分割字符串的时间复杂度是 O(m + n)，其中 m 和 n 分别是 version1 和 version2 的长度。
# 比较修订号的过程也是 O(m + n)，因为每个字符只会被处理一次。
# ✅ 总时间复杂度：O(m + n)

def compareVersion(version1: str, version2: str) -> int:
    # 分割版本号字符串
    parts1 = version1.split('.')
    parts2 = version2.split('.')

    # 获取两个版本号的最大长度
    i = 0
    while i < len(parts1) or i < len(parts2):
        # 获取当前修订号，注意处理超出索引的情况，默认值为0
        num1 = int(parts1[i]) if i < len(parts1) else 0
        num2 = int(parts2[i]) if i < len(parts2) else 0

        # 比较当前修订号
        if num1 > num2:
            return 1
        elif num1 < num2:
            return -1
        
        # 移动到下一个修订号
        i += 1

    # 如果所有修订号都相同，则返回0
    return 0