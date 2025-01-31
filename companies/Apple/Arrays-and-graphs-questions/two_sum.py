target = 5

# 2 + 3 = 5

# i  (t   j)
# 2 = 5 - 3

# dct = {}

def two_sum(arr, target = target):
    dct = {int:int}

    for (key, value) in enumerate(arr):
        if value in dct:
            print(dct[value], key)
        else:
            dct[target - value] = key
    return 

#       0  1  2  3
nums = [2, 4, 3, 8]
two_sum(nums)