def binary_search_rotated(nums:list, key:int):
    l = 0
    r = len(nums) - 1

    while l < r:
        mid = (l + r) // 2

        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m


