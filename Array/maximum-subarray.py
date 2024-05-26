class Solution:
    # Kadane's algorithm
    def kadane_algo(self, nums):
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)

        return maxSub

lst = [-2, -1, -3, 4, -1, 2, 1, -5, 4]

s = Solution()
print(s.kadane_algo(lst))