class Solution:
    def missing_number(self, nums):
        n = len(nums)
        e = (n * (n+1)) // 2
        s = sum(nums)

        return e - s        

nums = [4, 0, 1, 2]

s = Solution()
print(s.missing_number(nums))