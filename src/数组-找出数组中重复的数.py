
# 方法2     
def find_duplicates(nums):
    n = len(nums)
    result = []
    
    for i in range(n):
        while nums[i] != i:
            # 获取目标位置
            target_index = nums[i]
            
            # 检查是否超出范围或已经在正确位置
            if target_index < 0 or target_index >= n:
                break
            
            # 如果目标位置已经有相同的数字，说明找到重复数字
            if nums[target_index] == nums[i]:
                if nums[i] not in result:
                    result.append(nums[i])
                break
            
            # 否则交换当前值和目标位置的值
            nums[i], nums[target_index] = nums[target_index], nums[i]
    
    return result

# 示例测试
print(find_duplicates([4, 3, 2, 7, 8, 2, 3, 1]))  # 输出应该是 [2, 3]
print(find_duplicates([1, 1, 2]))                 # 输出应该是 [1]
print(find_duplicates([1]))                       # 输出应该是 []


# def is_duplicate_in_list(inputs):
#     "找出数组中重复的数字"
#     if len(inputs) == 0:
#         return -1

#     # 下标归位法
#     # 数组的长度为 n 且所有数字都在 0 到 n-1 的范围内，我们可以将每次遇到的数进行"归位"，当某个数发现自己的"位置"被相同的数占了，则出现重复。
#     # 扫描整个数组，当扫描到下标为 i 的数字时，首先比较该数字（m）是否等于 i，如果是，则接着扫描下一个数字；如果不是，则拿 m 与第 m 个数比较。
#     # 如果 m 与第 m 个数相等，则说明出现重复了；如果 m 与第 m 个数不相等，则将 m 与第 m 个数交换，将 m "归位"，再重复比较交换的过程，直到发现重复的数
#     # 以数组 {2,3,1,0,2,5,3} 为例, 当 i = 0 时，nums[i] = 2 != i，判断 nums[i] 不等于 nums[nums[i]]，交换 nums[i] 和 nums[nums[i]]，交换后数组为：{1,3,2,0,2,5,3}

#     for i ,value in enumerate(inputs):
#         # 如果索引等于当前的对应的值,说明该数是对的位置,无需调整归位
#         if i == value:
#             continue

#         tmp = inputs[value]

#         # 如果当前对应的值作为索引找到的值与当前的值不相等,就需要归位,两数位置做交换
#         if  value != tmp:
            
#             inputs[value] = value
#             inputs[i] = tmp
#         # 如果当前对应的值作为索引找到的值与当前值相等,说明已经有相同的值归位过,表示有重复的值
#         else:
            # return value



# 方法3
# 给你一个长度为 n 的整数数组 nums ，其中 nums 的所有整数都在范围 [1, n] 内，且每个整数出现 最多两次 。请你找出所有出现 两次 的整数，并以数组形式返回。
# 你必须设计并实现一个时间复杂度为 O(n) 且仅使用常量额外空间（不包括存储输出所需的空间）的算法解决此问题

def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
    
        for num in nums:
            index = abs(num) - 1  # 获取当前数字对应的索引
            
            if nums[index] < 0:  # 如果该位置已经是负数，说明这个数字已经出现过
                result.append(abs(num))
            else:
                nums[index] = -nums[index]  # 将该位置的值变为负数，表示这个数字已经出现过一次
        
        return result