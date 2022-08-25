# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2

# 解题思路
    # 双指针
    # 二分法

# 双指针
def func(array,target):
    left = 0
    right = 0
    n = len(array)

    sum = 0
    # 最大的一种情况，是数组长度个数值 相加才会大于 target，所以这里设置的要比数组长度大一些。
    res = n + 1

    while right < n:
        while (sum < target and right < n):
            sum += array[right]
            right += 1
        while (sum >= target):
            sum -= array[right]
            res = min(res,right - left + 1)
            left += 1

    return res

    
# 二分法
# // O(nlgn)
# 这个解法要用到二分查找法，
# 思路是，建立一个比原数组长一位的 sums 数组，其中 sums[i] 表示 nums 数组中 [0, i - 1] 的和，
# 然后对于 sums 中每一个值 sums[i]，用二分查找法找到子数组的右边界位置，使该子数组之和大于 sums[i] + s，
# 然后更新最短长度的距离即可。代码如下：
class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        int len = nums.size(), sums[len + 1] = {0}, res = len + 1;
        for (int i = 1; i < len + 1; ++i) sums[i] = sums[i - 1] + nums[i - 1];
        for (int i = 0; i < len + 1; ++i) {
            int right = searchRight(i + 1, len, sums[i] + s, sums);
            if (right == len + 1) break;
            if (res > right - i) res = right - i;
        }
        return res == len + 1 ? 0 : res;
    }
    int searchRight(int left, int right, int key, int sums[]) {
        while (left <= right) {
            int mid = (left + right) / 2;
            if (sums[mid] >= key) right = mid - 1;
            else left = mid + 1;
        }
        return left;
    }
};