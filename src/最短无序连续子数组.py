# 给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

# 请你找出符合题意的 最短 子数组，并输出它的长度。

# 输入：nums = [2,6,4,8,10,9,15]
# 输出：5
# 解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。

# 我们可以假设把这个数组分成三段，
# 左段和右段是标准的升序数组，中段数组虽是无序的，但满足中段的最小值大于左段的最大值，中段的最大值小于右段的最小值。

# 那么我们目标就很明确了，找中段的左右边界，我们分别定义为left 和 right;
# 分两头开始遍历:

# 从左到右维护一个最大值max,在进入右段之前，那么遍历到的nums[i]都是小于max的，
# 我们要求的right就是遍历中最后一个小于max元素的位置；

# 同理，从右到左维护一个最小值min，在进入左段之前，那么遍历到的nums[i]也都是大于min的，
# 要求的left也就是最后一个大于min元素的位置。

def findUnsortedSubarray( nums) -> int:
        n = len(nums)
        maxn, right = float("-inf"), -1
        minn, left = float("inf"), -1

        for i in range(n):
            if maxn > nums[i]:
                right = i
            else:
                maxn = nums[i]
            
            if minn < nums[n - i - 1]:
                left = n - i - 1
            else:
                minn = nums[n - i - 1]
        
        return 0 if right == -1 else right - left + 1
