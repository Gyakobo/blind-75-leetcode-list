class Solution:
    def solution(self, mtx):
        m = len(mtx)
        n = len(mtx[0])

        mtx.reverse() 

        for c in range(m):
            for r in range(c):
                mtx[r][c], mtx[c][r] = mtx[c][r], mtx[r][c] 

        return mtx

matrix = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]

# Desired output: [ [7, 4, 1], [8, 5, 2], [9, 6, 3] ]

s = Solution()
print(s.solution(matrix))
