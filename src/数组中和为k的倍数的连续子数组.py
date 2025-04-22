# 给定一个整数数组 nums 和一个整数 k ，返回其中元素之和可被 k 整除的（连续、非空） 子数组 的数目。

# 子数组 是数组的 连续 部分。

# 输入：nums = [4,5,0,-2,-3,1], k = 5
# 输出：7
# 解释：
# 有 7 个子数组满足其元素之和可被 k = 5 整除：
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

# 解题思路
    # 哈希表 + 逐一统计
    # 通常，涉及连续子数组问题的时候，我们使用前缀和来解决。
    # P[i]表示索引i在内的左侧所有数的和，根据 同余定理，只要 P[j] % k == P[i] % k ,则有P[j] - P[i] % k = 0 。
    
    # 需要注意的一个边界条件是，我们需要对哈希表初始化，记录 record[0] =1，
    # 这样就考虑了前缀和本身被 k 整除的情况。

class Solution:
    def subarraysDivByK(self, nums, k: int) -> int:
        record = {0: 1}
        total, res = 0, 0
        for elem in nums:
            total += elem
            modulus = total % k
            same = record.get(modulus, 0)
            res += same
            record[modulus] = same + 1
        return res

solu = Solution()

res = solu.subarraysDivByK([4,5,0,-2,-3,1],5)
print(res)