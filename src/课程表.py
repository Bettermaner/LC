# 1.课程表1
# 解题思路
    # 首先，搞清楚这个题目是要判断能否完成所有课程的学习，其实就是判断由课程作为节点构成的图是否为有向无环图，
    # 如果有环就不能完成课程学习，比如有两门课程，在学习1之前要学习0,那正好能完成两个课程，如果有环了，在完成1之前要完成0,在完成0之前要完成1,显然不可能。
    # 推广到多个课程，就是要构成有向无环图。

    # 这里使用辅助队列进行广度优先遍历，来判断是否为有向无环图，最后如果是有向无环图，所有节点都应该出队和入队过，出队次数应该等于课程次数，
    # 最后课程数应该是0。

    # 具体过程：
    # 由题目信息构建入度表和邻接表，数组模拟队列，将入度为0的节点加进队列里，然后如果队列非空，
    # 依次出队，并且将课程数减1,将出队元素原来连接的节点的入度减1,如果减完，度为0了，就加到队列里，继续循环，直到队列为空，跳出循环，返回结果。

def func(nums,prerequires):

    # 记录每个节点的入度
    courses = [0 for i in range(nums)]
    # 记录每个节点的邻居节点
    adj = [[] for i in range(nums)]

    # 队列
    queue = []

    # 建立入度表与邻接表
    for cur,pre in prerequires:
        courses[cur] += 1
        adj[pre].append(cur)

    # 将入度为0的节点取出，说明他们不需要先完成某些课程就可以完成。
    # 加入队列中
    for cur, value in enumerate(courses):
        if value == 0:
            queue.append(cur)

    # 若队列非空，就依次从队列中取出节点
    # 先进先出原则
    while queue:

        node = queue.pop(0)
        # 每出队一个节点，课程数-1
        nums -= 1

        for cur in adj[node]:
            # 将出队节点的连着的节点的入度-1，因为该节点已经取出，表示该课程已经完成
            courses[cur] -= 1
            
            # 如果减完后，入度为0了，说明可以接着完成该cur节点的课程
            # 继续放入队列中
            if courses[cur] == 0:
                queue.append(cur)

    if nums == 0:
        return True
    else:
        return False


# 课程表2
# 课程表 II
# 给定课程总量以及它们的先决条件，返回你为了学完所有课程所安排的学习顺序。

# 可能会有多个正确的顺序，你只要返回一种就可以了。如果不可能完成所有课程，返回一个空数组。

def func(nums,prerequires):

    # 记录每个节点的入度
    courses = [0 for i in range(nums)]
    # 记录每个节点的邻居节点
    adj = [[] for i in range(nums)]

    # 队列
    queue = []

    # 建立入度表与邻接表
    for cur,pre in prerequires:
        courses[cur] += 1
        adj[pre].append(cur)

    # 将入度为0的节点取出，说明他们不需要先完成某些课程就可以完成。
    # 加入队列中
    for cur, value in enumerate(courses):
        if value == 0:
            queue.append(cur)

    result = []
    # 若队列非空，就依次从队列中取出节点
    # 先进先出原则
    while queue:

        node = queue.pop(0)
        # 每出队一个节点，课程数-1
        nums -= 1
        result.append(node)

        for cur in adj[node]:
            # 将出队节点的连着的节点的入度-1，因为该节点已经取出，表示该课程已经完成
            courses[cur] -= 1
            
            # 如果减完后，入度为0了，说明可以接着完成该cur节点的课程
            # 继续放入队列中
            if courses[cur] == 0:
                queue.append(cur)

    if nums == 0:
        return result
    else:
        return []

print(func(4,[[1,0],[2,0],[3,1],[3,2]]))