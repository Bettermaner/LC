# 给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。
# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]

# 解题思路
    # 最小堆 + 哈希表
    
    # 首先遍历整个数组，并使用哈希表记录每个数字出现的次数，并形成一个「出现次数数组」。
    # 找出原数组的前 k 个高频元素，就相当于找出「出现次数数组」的前 k 大的值。

    # 最简单的做法是给「出现次数数组」排序。但由于可能有 O(N)个不同的出现次数（其中 N 为原数组长度），
    # 故总的算法复杂度会达到 O(N\log N)，不满足题目的要求。

    # 在这里，我们可以利用堆的思想：建立一个小顶堆，然后遍历「出现次数数组」：

    # 如果堆的元素个数小于 k，就可以直接插入堆中。
    # 如果堆的元素个数等于 k，则检查堆顶与当前出现次数的大小。
    # 如果堆顶更大，说明至少有 k 个数字的出现次数比当前值大，故舍弃当前值；否则，就弹出堆顶，并将当前值插入堆中。
    # 遍历完成后，堆中的元素就代表了「出现次数数组」中前 k 大的值。

def func(array,k):

    res = []
    hash_map = {}

    for v in array:
        hash_map[v] = hash_map.get(v,0) + 1

    count = list(hash_map.values())

    k_count = get_k_max(count,k)

    for v,c in hash_map.items():
        if c >= k_count:
            res.append(v)
    return res

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


print(func([1,1,1,2,2,3,4,3,3,2,1,4,5,5],2))