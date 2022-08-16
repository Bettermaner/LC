# 随意输入一个数字，用该数字内的数字组合出下一个比该数大的新数。
# 例如输入14321 下一个是 21134

# 解题思路
    # 数字从后往前找到第一次出现逆序的逆序对（就是右边的数字大于左边的数字，整体呈降序）
    # 然后交换该逆序对上的数
    # 再将该逆序对中前面的那个数，之后的所有数，进行排序（按照从小到大的升序排列）

def func(strings):

    n = len(strings)
    if n <= 1:
        return -1

    i,end = find(strings,n-1)
    if i == -1 and end == -1:
        return -1

    tmp = strings[end]
    strings[end] = strings[i]
    strings[i] = tmp

    strings = reverse(strings,i+1)
    return strings

def find(strings,end):

    while end >=1:
        i = end -1
        while i >=0:
            if strings[end] > strings[i]:
                return i,end
            i -= 1
        end -= 1
    return -1,-1


def reverse(strings,start):
    n = len(strings)
    for i in range(start,n):
        for j in range(i+1,n):
            if strings[i] > strings[j]:
                tmp = strings[i]
                strings[i] = strings[j]
                strings[j] = tmp
    return strings


print(func([2,4,3,2,1]))