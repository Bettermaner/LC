from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # 哈希表存储前缀和出现的次数
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1  # 初始化前缀和为0的情况
        
        count = 0  # 记录满足条件的子数组个数
        current_sum = 0  # 当前前缀和
        
        for num in nums:
            current_sum += num
            
            # 检查是否存在某个前缀和使得 current_sum - prefix_sum = k
            if current_sum - k in prefix_sums:
                count += prefix_sums[current_sum - k]
            
            # 更新当前前缀和的计数
            prefix_sums[current_sum] += 1
        
        return count