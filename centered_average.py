def centered_average(nums):
    bigNum=max(nums)
    smallNum=min(nums)
    mean=0
    for x in range(len(nums)):
        mean+=nums[x]
    mean=(mean-(bigNum+smallNum))/(len(nums)-2)
    return mean
