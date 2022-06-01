def re_order_array(inputs):
    "调整数组的顺序使得奇数在偶数前面,并且奇数与奇数、偶数与偶数之间相对的位置保持不变"

    # 输入一个长度为 n 整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前面部分，所有的偶数位于数组的后面部分，
    # 并保证奇数和奇数，偶数和偶数之间的相对位置不变。
    # 要求 时间复杂度(n**2), 空间复杂度(1)

    # 解题思路: 双指针
    # 偶数指针 找出数组中第一个偶数位置, 奇数指针找到数组中 第一个偶数右边的第一个奇数的位置
    # 然后 将当前奇数保存,把奇数到第一个偶数之间所有的数的下标往后移一格，最后将保存的奇数赋值到第一个偶数位置
    # 偶数指针向前移动一格，奇数指针继续前走，直到再次遇到奇数，重复上述的操作,直至奇数指针走到底
    if not inputs:
        return None

    l = len(inputs)

    odd_index = 0
    even_index = 0

    # 找出数组中第一个偶数位置
    while inputs[even_index] % 2 :
        even_index += 1

    # 找到数组中偶数位置右边的第一个奇数位置
    while inputs[odd_index] % 2 == 0 or odd_index < even_index:
        odd_index += 1

    while (odd_index < l and odd_index % 2 ):
        # 保存奇数
        tmp = inputs[odd_index]

        # 把奇数到第一个偶数之间所有的数的下标往后移一格
        tmp_odd_index = odd_index
        while(tmp_odd_index > even_index):
            inputs[tmp_odd_index] = inputs[tmp_odd_index-1]
            tmp_odd_index -= 1

        # 将保存的奇数赋值到第一个偶数位置
        inputs[even_index] = tmp

        # 偶数指针向前移动一格,因为当前位置指向奇数
        even_index += 1

        # 奇数指针继续前走，直到再次遇到奇数，重复上述的操作,直至奇数指针走到底,说明整个数组的奇数都移到了左边.
        while (odd_index < l and odd_index % 2 == 0):
            odd_index += 1

    return inputs
        

