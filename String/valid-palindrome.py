class Solution:
    # Time Complexity: O(n/2)
    def solution(self, word):
        if not word: return 

        n = len(word)

        for i in range(n//2):
            if word[i] != word[n-1-i]:
                return False
            
        return True 

s = Solution()
print(s.solution("abba"))