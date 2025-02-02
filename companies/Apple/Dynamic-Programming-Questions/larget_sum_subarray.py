def largest_sum_subarray(nums):
    maxSub = nums[0]    
    curSum = 0

    for n in nums:
        if curSum < 0
            curSum = 0  
        curSum += n

        maxSub = max(maxSub, curSum)

    return maxSub

nums = [-4, 2, -5, 1, 2, 3, 6, -5, 1]