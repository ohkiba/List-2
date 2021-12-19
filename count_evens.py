def count_evens(nums):
    count=0
    for x in range(len(nums)):
        if (nums[x]%2==0):
            count+=1
    return count