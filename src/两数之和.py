from os import stat


def two_sum(inputs,target):
    "两数之和"
    
    if len(inputs) < 2:
        return None

    tmp = {}
    for index,value in enumerate(inputs):
        remain_value = target - value
        if value not in tmp:
            tmp[remain_value] = index
        else:
            return (index,tmp[value])

# 另一个中方法，双指针
def two_sum(inputs,target):
    # 先对整体数组排序，从小到大进行排序。
    inputs.sort()

    start = 0
    end = len(inputs) -1


    while end > start:
        if inputs[start] + inputs[end] > target:
            end -= 1
        elif inputs[start] + inputs[end] < target:
            start += 1

        else:
            break
    if start == end:
        return 
    return inputs[start],inputs[end]


if __name__ == "__main__":
    print(two_sum([1,2,4,5,7],9))
