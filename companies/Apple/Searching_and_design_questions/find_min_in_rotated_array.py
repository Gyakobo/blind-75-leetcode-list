
def findMin(nums: list[int]) -> int:
    n = len(nums)
    res = nums[0]

    left    = 0
    right   = n-1 
    middle  = (right + left) // 2

    while left <= right:
        if nums[left] < nums[right]:
            res = min(res, nums[left]) 
            break

        middle = (right + left) // 2
        res = min(res, nums[middle])

        if nums[middle] >= nums[right]:
            left = middle + 1
        else:
            right = middle - 1

    return res 

nums = [3, 4, 5, 1, 2]
print(findMin(nums))
