def three_sum(nums):
    "三数之和"

    result = []
    n = len(nums)
    if n < 3:
        return result

    nums.sort()

    for i in range(0, n - 2):

        # 由于数组已经从小到大排过序，如果大于0，说明i索引后面的数据也大于0，直接跳出。
        if nums[i] > 0:
            break

        left = i + 1
        right = n - 1

        # 如果两个相邻的数相等，无需重复分析，直接跳到下一个索引。
        if i > 0 and nums[i] == nums[i-1]:
            continue

        while left < right:

            if nums[i] + nums[left] + nums[right] == 0:
                result.append([nums[i], nums[left], nums[right]])
                right -= 1
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1
                while nums[right] == nums[right + 1] and left < right:
                    right -= 1

            elif nums[i] + nums[left] + nums[right] > 0:
                right -= 1

            elif nums[i] + nums[left] + nums[right] < 0:
                left += 1

    return result


if __name__ == "__main__":
    print(three_sum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]))
