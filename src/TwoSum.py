def two_sum(inputs,target):

    if len(inputs) < 2:
        return None

    tmp = {}
    for index,value in enumerate(inputs):
        remain_value = target - value
        if value not in tmp:
            tmp[remain_value] = index
        else:
            return (index,tmp[value])

if __name__ == "__main__":
    print(two_sum([1,2,4,5,7],9))
