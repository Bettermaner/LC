def cut_rope(rope_length):
    "剪绳子,剪成若干份后(必须要分成>1段),各部分绳子长度相乘 乘积最大"

    # 解题思路: 动态回归
    # 一旦分出一段长度为1的小段，只会减少总长度，还不能增加乘积，因此长度为2的绳子不分比分开的乘积大，长度为3的绳子不分比分开的乘积大，长度为4的绳子分成2*2比较大。前面的我们都可以通过这样递推得到，后面的呢？
    # 同样递推！如果我有一个长度为nnn的绳子，我们要怎么确定其分出最大的乘积，我们可以尝试其中一段不可分的为j，那么如果另一段n-j最大乘积已知，我们可以遍历所有j找到这个最大乘积。
    # 因此用dp[i]表示长度为i的绳子可以被剪出来的最大乘积，

    if rope_length <=  3:
        return rope_length - 1

    # 用dp[i]表示长度为i的绳子可以被剪出来的最大乘积
    dp = [0 for i in range(rope_length + 1)]
    dp[1],dp[2],dp[3],dp[4] = 1,2,3,4
    
    # 那么后续遍历每个j的时候，我们取最大dp[i]=max(dp[i],j∗dp[i−j])dp[i] = max(dp[i], j * dp[i - j])dp[i]=max(dp[i],j∗dp[i−j])就好了。
    for i in range(5,rope_length+1):
        for j in range(i):
            dp[i] = max(dp[i],dp[i -j] * dp[j]) 

    return dp[rope_length]