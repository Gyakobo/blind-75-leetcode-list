class Solution:
    def missing_number(self, nums):
        n = len(nums)
        s = sum(nums)
        e = (n * (n+1)) // 2

        return e - n         

nums = [3, 0, 1]

s = Solution()
print(s.missing_number(nums))