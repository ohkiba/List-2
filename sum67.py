def sum67(nums):
    count=0
    x=0

    while x<len(nums):
        if nums[x]!=6:
            count+=nums[x]
        else:
            while nums[x]!=7:
                x+=1
        x+=1
    return count
