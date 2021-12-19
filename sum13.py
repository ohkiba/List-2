def sum13(nums):
    count=0
    x=0
    if (len(nums)>0):
        while x<len(nums):
            if nums[x]!=13:
                    count+=nums[x]
            else:
                x+=1
            x+=1
    return count

