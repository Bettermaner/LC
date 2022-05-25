def is_duplicate_in_list(inputs):
    "找出数组中重复的数字"
    if len(inputs) == 0:
        return -1

    # 下标归位法
    # 数组的长度为 n 且所有数字都在 0 到 n-1 的范围内，我们可以将每次遇到的数进行"归位"，当某个数发现自己的"位置"被相同的数占了，则出现重复。
    # 扫描整个数组，当扫描到下标为 i 的数字时，首先比较该数字（m）是否等于 i，如果是，则接着扫描下一个数字；如果不是，则拿 m 与第 m 个数比较。
    # 如果 m 与第 m 个数相等，则说明出现重复了；如果 m 与第 m 个数不相等，则将 m 与第 m 个数交换，将 m "归位"，再重复比较交换的过程，直到发现重复的数
    # 以数组 {2,3,1,0,2,5,3} 为例, 当 i = 0 时，nums[i] = 2 != i，判断 nums[i] 不等于 nums[nums[i]]，交换 nums[i] 和 nums[nums[i]]，交换后数组为：{1,3,2,0,2,5,3}

    for i ,value in enumerate(inputs):
        # 如果索引等于当前的对应的值,说明该数是对的位置,无需调整归位
        if i == value:
            continue

        tmp = inputs[value]

        # 如果当前对应的值作为索引找到的值与当前的值不相等,就需要归位,两数位置做交换
        if  value != tmp:
            
            inputs[value] = value
            inputs[i] = tmp
        # 如果当前对应的值作为索引找到的值与当前值相等,说明已经有相同的值归位过,表示有重复的值
        else:
            return value
