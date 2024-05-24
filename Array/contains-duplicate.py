class Solution:
    # Using a hashset
    def contains_duplicate(nums):
        arr = set() # O(1) - time complexity
        
        for val in nums:
            if val not in arr:
                arr.add(val)
            else:
                return True
        
        return False

lst = [1, 2, 3, 1]