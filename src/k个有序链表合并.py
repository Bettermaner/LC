# 解题思路
    # 最小堆解决
    # 1.将所有的链表数据依次放入到最小堆中，最后得到含有所有数的最小堆
    # 2.取出堆顶的数，然后重新构建最小堆
    # 3.重复进行上面的2操作，直至堆里没有数据。完成从小到大的排序

    # 伪代码
def merge(k_array):

    for array in k_array:
        while array:
            heap.push(array)
            array = array.next
    
    node = Tree()
    head = node

    while heap:
        min_node = heap.pop()
        head.next = min_node
        head = head.next

    return node.next