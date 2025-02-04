
target = 7

# i   j 
# 2 + 5 = 7 

# i    t - j
# 2 = (7 - 5) 

def two_sum(arr, target = target):
    hashmap = {int: int}

    for (key, value) in enumerate(arr):
        if value in hashmap:
            print(key, hashmap[value])
            break
        else:
            hashmap[target - value] = key

nums = [2, 3, 4, 5, 6, 7]
two_sum(nums) 