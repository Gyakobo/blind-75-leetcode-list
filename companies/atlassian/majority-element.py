array = [3, 3, 2, 3, 1]

# Moore's voting algorithm
# The devil is in the description - the majority element is strictly an element which can be
# encoutered more than n>2
def majority_element(arr):
    n = len(arr)
    candidate = -1
    count = 0

    # Find a candidate
    for num in arr:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    # Validate the candidate
    count = 0
    for num in arr:
        if num == candidate:
            count += 1

    # If count is greater than n / 2, return the candidate; otherwise, return -1
    if count > n // 2:
        return candidate
    else:
        return -1

print(array)
print(f"Max freq: {majority_element(array)}")