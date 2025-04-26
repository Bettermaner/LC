# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2

# 解题思路
    # 双指针
    # 二分法

# 1.双指针（只能解决数组中无负数的情况）
def func(array,target):
    left = 0
    n = len(array) -1

    sum = 0
    # 最大的一种情况，是数组长度个数值 相加才会大于 target，所以这里设置的要比数组长度大一些。
    res = n + 1

    for i in range(len(array)):
        sum += array[i]
        while sum > target and left <= i:
            res = min(res,i - left + 1)
            sum -= array[left]
            left += 1

    return res

print(func([2,4,1,2,4,4],7))


# 2.双端队列+前缀和（能解决所有情况，包括有正数，有负数）

# 前缀和数组：prefix_sums[i]表示从数组开始到第i-1个元素的累积和。这样可以快速计算任意子数组的和。
# 模拟双端队列：
# 使用一个列表q来存储前缀和的索引。
# 当前前缀和减去队列头部的前缀和大于等于k时，更新最短长度，并移除队列头部元素（相当于popleft操作）。
# 维护队列中的前缀和有序性，确保队列内的元素按照前缀和递增顺序排列。如果当前前缀和小于等于队列尾部的前缀和，则移除队列尾部元素

def minSubarrayLen(nums, k):
    n = len(nums)
    prefix_sums = [0] * (n + 1)  # 前缀和数组，prefix_sums[i]表示nums[0:i]的和
    min_length = float('inf')  # 初始化为无穷大
    
    # 计算前缀和
    for i in range(1, n + 1):
        prefix_sums[i] = prefix_sums[i - 1] + nums[i - 1]
    
    # 模拟双端队列使用的列表
    q = []
    
    for i in range(n + 1):
        # 当前前缀和减去队列头部的前缀和大于等于k时，更新最小长度
        while q and prefix_sums[i] - prefix_sums[q[0]] >= k:
            min_length = min(min_length, i - q.pop(0))
        
        # 维护队列中的前缀和有序性
        while q and prefix_sums[i] <= prefix_sums[q[-1]]:
            q.pop()
        
        q.append(i)
    
    return min_length if min_length != float('inf') else -1
    
# 二分法
# // O(nlgn)
# 这个解法要用到二分查找法，
# 思路是，建立一个比原数组长一位的 sums 数组，其中 sums[i] 表示 nums 数组中 [0, i - 1] 的和，
# 然后对于 sums 中每一个值 sums[i]，用二分查找法找到子数组的右边界位置，使该子数组之和大于 sums[i] + s，
# 然后更新最短长度的距离即可。代码如下：
# class Solution {
# public:
#     int minSubArrayLen(int s, vector<int>& nums) {
#         int len = nums.size(), sums[len + 1] = {0}, res = len + 1;
#         for (int i = 1; i < len + 1; ++i) sums[i] = sums[i - 1] + nums[i - 1];
#         for (int i = 0; i < len + 1; ++i) {
#             int right = searchRight(i + 1, len, sums[i] + s, sums);
#             if (right == len + 1) break;
#             if (res > right - i) res = right - i;
#         }
#         return res == len + 1 ? 0 : res;
#     }
#     int searchRight(int left, int right, int key, int sums[]) {
#         while (left <= right) {
#             int mid = (left + right) / 2;
#             if (sums[mid] >= key) right = mid - 1;
#             else left = mid + 1;
#         }
#         return left;
#     }
# };