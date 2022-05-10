def three_sum(inputs):
    
    n = len(inputs)
    result = []


    for i,value in enumerate(inputs):
        left = i + 1
        right = n -1

        while left < right:
            sum =  inputs[left] + inputs[right] + inputs[i]
            if sum == 0:
                result.append(i,left,right)
                left += 1
                right -= 1

            elif sum < 0 :
                left += 1
            elif sum > 0 :
                right -= 1

        return result
