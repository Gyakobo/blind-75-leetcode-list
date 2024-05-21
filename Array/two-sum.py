class Solution:
    def __init__(self):
        pass

    # Pointer Solution
    def twoSum_pointer(self, nums, target: int):
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

    # Hashmap Solution
    def twoSum_hashmap(self, nums, target: int):
        dct = {int:int} 
        for i, element in enumerate(nums):
            if element in dct:
                return [dct[element], i]
            else:
                dct[target-element] = i 

func = Solution()
my_lst = [2, 4, 3, 1] 
my_target = 5

print(func.twoSum_hashmap(my_lst, my_target))
