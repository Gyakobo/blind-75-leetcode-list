
s = "aaaaa"

def palindrome_substrings(s = s):
    # Miscellaneous 
    n = len(s)    
    res = []

    left = 0
    right = 0
    i = 0

    for i in range(n):
        left    = i - 1
        right   = i + 1
        res.append(s[i])      

        while left >= 0 and right < n and s[left] == s[right]:
            print("pointer1:", left, right, ":", s[left:right+1])
            res.append(s[left: right+1])
            left    -= 1
            right   += 1

        left    = i
        right   = i + 1
        while left >= 0 and right < n and s[left] == s[right]:
            print("pointer2:", left, right, ":", s[left:right+1])
            res.append(s[left: right+1])
            left    -= 1
            right   += 1

    return res

print(palindrome_substrings(s))
