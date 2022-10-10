# 给你一个会议时间安排的数组 intervals ，
# 每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi] ，返回 所需会议室的最小数量 。

# 输入：intervals = [[0,30],[5,10],[15,20]]
# 输出：2

#解题思路
    # 最小堆 
    # 排序过程很容易，但对每个会议，我们如何高效地找出是否有房间可用？
    # 任意时刻，我们都有多个可能占用的房间，只要我们能在有新会议需要时就找到一个空闲房间，
    # 我们并不需要关心到底有哪些房间是空闲的。
    # 一个朴素的方法是，每当有新会议时，就遍历所有房间，查看是否有空闲房间。

    # 1.按照 开始时间 对会议进行排序。
    # 2.初始化一个新的 最小堆，将第一个会议的结束时间加入到堆中。我们只需要记录会议的结束时间，告诉我们什么时候房间会空。
    # 3.对每个会议，检查堆的最小元素（即堆顶部的房间）是否空闲（比较当前遍历到的会议的起始时间 是否大于 堆的最小元素的结束时间）。
    # 4.若房间空闲，则从堆顶拿出该元素，将其改为我们处理的会议的结束时间，加回到堆中。若房间不空闲。开新房间，并加入到堆中。
    # 5.处理完所有会议后，堆的大小即为开的房间数量。这就是容纳这些会议需要的最小房间数。


# 构建堆
from cProfile import label


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


def func(intervals):

    if not intervals:
        return 0

    free_room = []

    # 按照会议的起始时间从小到大排序
    intervals.sort(key=lambda x: x[0])

    # 将最先开始的会议先放入堆中
    free_room.append(intervals[0][1])
    build_min_heap(free_room)

    # 对每个会议，检查堆的最小元素（即堆顶部的房间）是否空闲（比较当前遍历到的会议的起始时间 是否大于 堆的最小元素的结束时间）。
    for meeting in intervals[1:]:

        # 若房间空闲，则从堆顶拿出该元素，将其改为我们处理的会议的结束时间，加回到堆中。
        if meeting[0] >= free_room[0]:
            free_room.pop(0)
            build_min_heap(free_room)

        # 若房间不空闲。开新房间，并加入到堆中。
        free_room.append(meeting[1])
        build_min_heap(free_room)

    return len(free_room)


print(func([[0,30],[5,10],[15,20]]))