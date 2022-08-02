# 解题思路
    # 分而治之（二分）
    # 求第k大的数，我们设这k个数，包含在数组a中的有p个，包含b中的有q个，则有p+q=k; a数组的起始索引astart = 0，b数组的起始索引bstart=0
    # 那么怎么确定p呢，我们设p = min（k/2，m）,这里我们假设m是比较短的那个数组的长度，取p= k/2和m的较小者，保证数组不越界。则q=k-p
    # 以 a b 为例 m = 3，n = 6； 假如要求中位数（k=4）；p=min（k/2，m）= 2，q= k-p=2
    # 如果 a[astart+p-1] < b[bstart+q-1]; k= k-p, 我们就可以把a数组中包括索引p在内的比较小的数都抛弃，形成一个新的数组a' 与 b 再来一次上述过程，
    # 如果a[astart+p-1] > b[bstart+q-1]; k= k- q , 就抛弃b中的较小的数 形成一个新的数组b'，与a再来一次；如果相等 那这个数就是要找的中位数

    # 循环的结束条件是 
    # 1.当如果较短的数组长度为0（比如a数组）了，则返回b[bstart+k-1]; 
    # 2. 如果k==1了 则返回 a[astart]与b[bstart]中的较小者

def func(short_array1,long_array2,short_start,long_start,k):
    if len(short_array1) > len(long_array2):
        func(long_array2,short_array1,long_start,short_start)

    if len(short_array1) == 0:
        return long_array2[long_start+k-1]

    if k == 1:
        return short_array1[0]  if long_array2[0] > short_array1[0] else long_array2[0]

    p = min(k/2,len(short_array1))
    q = k - p

    if short_array1[short_start+p-1] > long_array2[long_start+q-1]:
        func(short_array1,long_array2[q+1:],short_start,long_start+q,k-q)
    elif short_array1[short_start+p-1] < long_array2[long_start+q-1]:
        func(short_array1[p+1:],long_array2,short_start+p,long_start,k-p)

    else:
        return short_array1[short_start+p-1]