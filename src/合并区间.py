# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

# 解题思路
    # 排序

def func(array):
    # 首先先按照每个区间的左边界从小到大的排序
    array.sort(key=lambda x:x[0])

    merge = []

    for inter in array:
        if not merge or merge[-1][1] < inter[0]:
            merge.append(inter)
        else:
            merge[-1][1] = max(merge[-1][1],inter[1])

    return merge

print(func([[1,3],[2,6],[8,10],[15,18]]))