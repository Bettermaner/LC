# 解题思路
    # 那可以反过来我不以每个块为处理单元，而是以块的四周作为处理单元
    # 那如何保证所有四周的可能性都考虑到呢？ 我们从矩阵的最外围往里面遍历，像一个圈不断缩小的过程
    # 为了防止重复遍历用visited记录
    # 其次要用小顶堆(以高度为判断基准)来存入所有快的四周(即圈是不断缩小的，小顶堆存的就是这个圈)
    # 为什么要用小顶堆？ 这样可以保证高度较小的块先出队
    # ** 为什么要让高度较小的块先出队？(关键点)
    # 一开始时候就讲了基础做法是：对于每一个块，去找它四个方向最高的高度中的最小值(二维下则是左右最高的高度取较小的那一个)作为上界，当前块作为下界
    # 而我们现在反过来不是以中心块为处理单元，而是以四周作为处理单元
    # 我们如果能确保当前出队的元素对于该中心块来说是它周围四个高度中的最小值那么就能确定接雨水的大小
    # 为什么队头元素的高度比中心块要高它就一定是中心块周围四个高度中的最小值呢？
    # 因为我们的前提就是小顶堆：高度小的块先出队，所以对于中心块来说，先出队的必然是中心块四周高度最小的那一个
    # 步骤：
    # 构建小顶堆，初始化为矩阵的最外围(边界所有元素)
    # 不断出队，倘若队头元素大于其四周的
    # 即代表能够接雨水：队头元素减去该中心块即当前中心块能接雨水的值
    # 但是接完雨水之后中心块还要存进队列中，但这时要存入的中心块是接完雨水后的中心块

def func(heigh):

    if len(heigh) <= 2 or len(heigh[0]) <= 2:
        return 0

    m = len(heigh)
    n = len(heigh[0])

    visit = [[ False  for j in range(n)] for i in range(m)]
    # 最小堆 heap
    # 遍历找出最外层方块加入到最小堆中，并找出最外层的最小高度
    for i in range(m):
        for j in range(n):
            if (i == 0 or j == 0 or i == m-1 or j == n-1):
                heap.add(i*n+j,heigh[i][j])
                visit[i][j] = True

    
    result = 0
    dis = [-1,0,1,0,-1]

    while heap:
        
        cur = heap.poll()
        i = cur[0] / n
        j = cur[0] % n

        for k in range(4):
            x = i + dis[k]
            y = j + dis[k+1]
            if (x>=0 and y >=0 and x<=m-1 and y<=n-1 and not visit[i][j]):
                if cur[1] > heigh[x][y]:
                    result += cur[1] - heigh
            heap.add(x*n + y,max(heigh[i][j],cur[1]))
            visit[x][y] = True

    return result
                



