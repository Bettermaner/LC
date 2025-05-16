def get_k_max(inputs,k):
    "最大k个值"

    if len(inputs) < k or len(inputs) == 0:
        return inputs

    heap = inputs[:k]

    build_min_heap(heap)

    for i in range(k,len(inputs)):
        if heap[0] < inputs[i]:
            heap[0] = inputs[i]
            min_heapify(heap,k,0)

    return heap[0]


def build_min_heap(heap):
    length = len(heap)

    for i in range(int(length/2 -1),-1,-1):
        min_heapify(heap,length,i)


def min_heapify(heap,length,root):
    min = root
    left = 2 * root + 1
    right = 2* root + 2

    if  length > left and heap[min] > heap[left] :
        min = left
    if length > right and heap[min] > heap[right]:
        min = right
    if min != root:
        heap[root],heap[min] = heap[min],heap[root]
        min_heapify(heap,len(heap),min)
    

if __name__ == "__main__":
    inputs = [16,1,2,3,1,5,4,7,8,9,22,3,54,13,11,20,12,4,5,6,25]
    k = 6
    print(get_k_max(inputs,k))



# ✅ 思路说明：
# 我们要找的是数组中 第 k 大的元素，可以转换为：

# 数组排序后，从右往左数第 k 个元素。
# 或者等价于：找数组中第 (n - k) 小的元素（升序排列后的索引为 n - k 的那个数）。
# 我们使用 快速选择（QuickSelect） 算法，它只对包含目标元素的那一侧进行递归划分，而不是像快速排序那样对全部元素排序。

# ✅ 时间复杂度分析：
# 平均时间复杂度：O(n)
# 最坏情况：当每次划分都极不平衡时，复杂度为 O(n^2)（但随机选择 pivot 能极大降低这种情况的概率）

import random

def partition(arr, left, right):
    """
    快速排序的分区函数，将比 pivot 小的放左边，大的放右边
    返回 pivot 最终所在的位置
    """
    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] < pivot:
            # 这样做的结果是：始终保证从 left 到 i - 1 的元素都小于 pivot。
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    # 现在，i 左边的元素都小于 pivot，右边的都大于等于它。
    arr[i], arr[right] = arr[right], arr[i]
    return i

def quick_select(arr, left, right, k_index):
    """
    使用 QuickSelect 找到第 k 小的元素（k_index 是升序排列中的索引）
    """
    if left == right:  # 只有一个元素
        return arr[left]

    # 随机选择 pivot 并交换到最后一个位置
    pivot_index = random.randint(left, right)
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]

    pivot_index = partition(arr, left, right)

    if k_index == pivot_index:
        return arr[k_index]
    elif k_index < pivot_index:
        return quick_select(arr, left, pivot_index - 1, k_index)
    else:
        return quick_select(arr, pivot_index + 1, right, k_index)

def find_kth_largest(arr, k):
    """
    找出数组中第 k 大的元素
    """
    n = len(arr)
    assert 1 <= k <= n, "k must be between 1 and the length of the array"
    return quick_select(arr, 0, n - 1, n - k)

# 示例用法：
arr = [3, 2, 1, 5, 6, 4]
k = 2
print(f"数组中第 {k} 大的数是：{find_kth_largest(inputs, 6)}")


