
def knapasack_problem(weights, values, container):
    "背包问题 (动态规划)"

    # None 表示第0个物品
    # ['None', {'w': 1, 'v': 3}, {'w': 3, 'v': 4}, {'w': 5, 'v': 8}, {'w': 7, 'v': 8}, {'w': 9, 'v': 10}]
    tr = ['None'] + [{"w": w, "v": v}for w, v in zip(weights, values)]

    # 背包最大容量
    container

    # 生成二维表
    # 表格从0个物品，0个背包容量开始表示
    table = {(i, w): 0 for i in range(len(tr))
             for w in range(container + 1)}

    # 开始动态规划
    # i = 0或者w=0时,最大价值必定为0
    # 所以从第1个物品，背包容量为1开始计算
    for i in range(1, len(tr)):

        for w in range(1, container + 1):
            # 当第i个物品 大于当前的背包容量时，则选择不放进背包
            # 此时最大价值等于 （当前的背包容量下的i-1个物品的最大价值，因为第i个物品没放）
            if tr[i]["w"] > w:
                table[(i, w)] = table[(i-1, w)]
            else:
                # 如果第i个物品小于于当前的背包容量时
                # 情况一，将当前第i个物品放入背包，算出i物品的价值，再根据剩余背包的容量，回溯到当放i-1个物品时所有的最高价值，两者相加为最终的价值
                # 情况二，将当前第i个物品不放入背包，此时最大价值等于（当前的背包容量下的i-1个物品的最大价值，因为第i个物品没放）
                # 根据情况一、情况二比较后取最大的价值
                table[(i, w)] = max(table[i-1, w], tr[i]
                                    ['v'] + table[(i-1, w - tr[i]['w'])])

    # 最大价值对应二维表格的右下角位置，表示尝试了放入n个物品后，在容量m下能表示的最大价值
    max_value = table[(len(tr)-1, container)]

    result = []
    num = len(tr) - 1
    c = container
    while num > 0:
        if table[(num, c)] == table[(num-1, c)]:
            num -= 1
            continue
        else:
            result.append(tr[num])
            c = c - tr[num]['w']
            num -= 1

    return max_value, result


if __name__ == "__main__":

    weights = [1, 3, 5, 7, 9]
    values = [3, 4, 8, 8, 10]
    container = 20
    print(knapasack_problem(weights, values, container))
