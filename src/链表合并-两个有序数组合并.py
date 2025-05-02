# 请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
# 注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。
# 为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。




# 由于 nums1 后面有足够空间容纳 nums2，我们不需要额外空间。可以利用三个指针从后往前比较、插入：

# 指针 i：指向 nums1 的有效末尾（即 m - 1）。
# 指针 j：指向 nums2 的末尾（即 n - 1）。
# 指针 k：指向 nums1 的最后位置（即合并后的末尾），用于填充较大值。
 # 每次比较 nums1[i] 和 nums2[j]，把较大的那个放到 nums1[k] 处，并移动相应指针。

# 时间复杂度：O(m + n)，每个元素都只访问一次。
# 空间复杂度：O(1)，原地修改 nums1，没有使用额外空间。

def merge(nums1, m: int, nums2, n: int) -> None:
    i = m - 1
    j = n - 1
    k = m + n - 1  # 最终填充的位置

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # 如果 nums2 还有剩余元素，复制过去
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

# 测试示例
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

merge(nums1, m, nums2, n)
print(nums1)  # 输出: [1, 2, 2, 3, 5, 6]



# 有序数组合并，无提前设置m+n的空间的情况
def mergeTwoSortedArrays(nums1, nums2):
    m, n = len(nums1), len(nums2)
    i, j = 0, 0
    result = []

    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1

    # 添加剩余元素
    result.extend(nums1[i:])
    result.extend(nums2[j:])

    return result

# 示例
nums1 = [1, 2, 3]
nums2 = [2, 5, 6]
print(mergeTwoSortedArrays(nums1, nums2))
# 输出: [1, 2, 2, 3, 5, 6]