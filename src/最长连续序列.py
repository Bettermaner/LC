# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9

# 解题思路
    # 哈希表

def func(array):

    if not array:
        return 0
    
    num_set = set(array)  # 使用集合代替字典，因为我们只关心键的存在性
    longest_streak = 0
    
    for num in num_set:
        # 只有当num是某个连续序列的第一个数时才进入循环
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            
            longest_streak = max(longest_streak, current_streak)
    
    return longest_streak


print(func([0,3,7,2,5,8,4,6,0,1]))