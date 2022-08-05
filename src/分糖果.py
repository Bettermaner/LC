# 1
# 给定一个偶数长度的数组，其中不同的数字代表着不同种类的糖果，每一个数字代表一个糖果。
# 你需要把这些糖果平均分给一个弟弟和一个妹妹。返回妹妹可以获得的最大糖果的种类数。
def func(candies):
    candies = sorted(candies,key=lambda x:x)
    count = 1
    n = len(candies)

    for i in range(n-1):
        if candies[i] != candies[i+1]:
            count += 1

    return min(n/2,count)


# 2
# n 个孩子站成一排。给你一个整数数组 ratings 表示每个孩子的评分。
# 你需要按照以下要求，给这些孩子分发糖果：
#每个孩子至少分配到 1 个糖果。
# 相邻两个孩子评分更高的孩子会获得更多的糖果。
# 请你给每个孩子分发糖果，计算并返回需要准备的 最少糖果数目 。

# 贪心算法
# 先对candy数据均用1填充
# 遍历ratings数组，如果右边的值大于左边的值，candy[i] = candy[i-1]+1;
# 再遍历ratings数组，如果左边的值大于右边的值，取candy[i] = max(candy[i + 1] + 1, candy[i])
# 再对candy数组求和即可

def func(ratings):
    n = len(ratings)

    candies = [1 for i in range(n)]

    for i in range(1,n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1

    for i in range(n-1):
        if ratings[i+1] < ratings[i]:
            candies[i] = max(candies[i+1] + 1,candies[i])

    result = sum(candies)
    return result


# https://blog.csdn.net/qq_53226437/article/details/124001836?spm=1001.2101.3001.6650.3&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-3-124001836-blog-117374037.pc_relevant_multi_platform_featuressortv2removedup&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-3-124001836-blog-117374037.pc_relevant_multi_platform_featuressortv2removedup&utm_relevant_index=6