def big_diff(nums):
    bigNum=0
    smallNum=0
    for x in range(len(nums)):
        bigNum=max(nums)
        smallNum=min(nums)
    return bigNum-smallNum