def findAllPeeks(nums):
    ret = []
    for i in range(1, len(nums) - 1):
        if nums[i - 1] < nums[i] >= nums[i + 1]:
            ret += [nums[i]]
    return ret

input=[1,2,3,2,1,-1,3,4,2,3,3,3]
input=[1,1,2,2,2,2]
input=[1,3,2,4,4,4,4]
print(findAllPeeks(input))