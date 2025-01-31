target = 20

def three_sum(arr, target = target):
    # Misc
    res = []
    n = len(arr)

    # Pointers
    i = 0
    low = i + 1
    high = n - 1

    # Main cycle
    arr.sort() # nlogn 
    print("Array:", arr)

    for i in range(n-2):
        low = i + 1
        high = n - 1

        while low < high:
            total = arr[i] + arr[low] + arr[high]

            if total == target:
                res.append( (arr[i], arr[low], arr[high]) )
                break
            elif total > target:
                high -= 1
            elif total < target:
                low += 1
    
    return res

#       i     l->       <-h
nums = [3, 7, 1, 2, 8, 4, 5, 10, 10, 15, 5]

print(three_sum(nums))

