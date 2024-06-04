class Solution:
    def group_anagrams(self, words):
        if not words: return 

        dct = {}

        for word in words:
            sort_word = ''.join(sorted(word))
            if sort_word not in dct:
                dct[sort_word] = [word]
            else:
                dct[sort_word].append(word)

        return dct.values()

strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

s = Solution()
print(s.group_anagrams(strs))
