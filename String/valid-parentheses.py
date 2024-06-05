class Solution:
    def valid_parentheses(self, string):
        if not string: return False

        dct = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        # O(n) time complexity
        stack = [] 
        for c in string:
            if c in dct.keys():
                if stack and stack[-1] == dct[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True

string = "()[]{}}}}"
s = Solution()
print(s.valid_parentheses(string))

