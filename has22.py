def has22(nums):
    x=0
    while x<len(nums)-1:
        if nums[x]==2 and nums[x+1]==nums[x]:
            return True
        x+=1
    return False