target = 20

def three_sum(arr, target = target):
    n = len(arr)
    res = [] 

    # Pointers to indices  
    i = 0
    low = i+1 
    high = n-1 

    # Main Operation
    arr.sort() # nlogn 
    print("Array:", arr)

    for i in range(n-2):
        while low != high:
            total = arr[i] + arr[low] + arr[high]
            print(i, total)

            if total == target:
                res.append([i, low, high])
            elif total < target:
                low += 1
            elif total > target:
                high -= 1
            elif low == high:
                low = i + 1
                high = n - 1 
                # break 
        
    return res

#       i     l->       <-h
nums = [3, 7, 1, 2, 8, 4, 5]

print(three_sum(nums))