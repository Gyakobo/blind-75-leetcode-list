def binary_search_rotated(nums:list[int], key:int) -> int:
    n = len(nums)

    min_index = 0
    middle = 0
    left = 0
    right = 0

    while left < right:
        middle = (left + right) // 2

        if nums[middle] > nums[right]:
            left = middle + 1
        else:
            right = middle

    min_index = left

    return min_index


