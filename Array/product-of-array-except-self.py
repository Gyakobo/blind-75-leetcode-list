class Solution:
    def solution(self, nums):
        n = len(nums)
        res = [1] * n

        pre = post = 1

        res[0] = pre
        for i in range(n-1):
            pre *= nums[i]
            res[i+1] = pre

        for i in range(n-1, 0, -1):
            post *= nums[i]
            res[i-1] *= post

        return res 

lst = [1, 2, 3, 4]

s = Solution()
print(s.solution(lst))
