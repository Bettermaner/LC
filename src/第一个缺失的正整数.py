# 解题思路
    # 先找出所有值小于等于该数组长度的数字，并将其按照数字的大小当做索引，插入到数组对应的位置中
    # 然后再遍历一遍数组，将第一次出现 （当前数字的值和当前数组的索引不相等时），返回当前索引+ 1 大小即可。


import copy
def run(nums):

  for i in range(len(nums)):
          if nums[i] < 0:
            nums[i] = len(nums) + 2

  arr = copy.deepcopy(nums)
  
  for index , value in enumerate(nums):
      cor = value -1
      if cor != index and cor > 0 and cor <= len(nums):
          tmp = arr[cor]
          arr[cor] = value
          arr[index] = cor
    
  for index ,value in enumerate(arr):
      if index != value -1:
        return index + 1


  return len(nums) + 1

print(run([7,8,9,11,12]))
print(run([1,2,0]))
print(run([3,4,-1,1]))