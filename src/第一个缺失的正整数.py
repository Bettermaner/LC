# 解题思路
    # 先找出所有值小于等于该数组长度的数字，并将其按照数字的大小当做索引，插入到数组对应的位置中
    # 然后再遍历一遍数组，将第一次出现 （当前数字的值和当前数组的索引不相等时），返回当前索引+ 1 大小即可。


def run(nums):
  n = len(nums)
        
  # 第一步：标记不在范围内的数和调整数组使得每个数尽量放在对应的位置上
  for i in range(n):
      while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
          # Swap nums[i] with the number at its target position.
          nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

  # 第二步：查找第一个不符合条件的位置
  for i in range(n):
      if nums[i] != i + 1:
          return i + 1

  # 如果所有位置都符合条件，则返回n+1
  return n + 1

print(run([7,8,9,11,12]))
print(run([1,2,0]))
print(run([3,4,-1,1]))