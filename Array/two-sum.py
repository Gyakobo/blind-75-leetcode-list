# Pointer Solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a_pointer = 0
        b_pointer = len(nums) - 1

        while (a_pointer <= b_pointer):
            sum = nums[a_pointer] + nums[b_pointer]

            if (sum > target):
                b_pointer -= 1
            elif (sum < target):
                a_pointer += 1    
            else:
                return [a_pointer, b_pointer]

        return [a_pointer, b_pointer]