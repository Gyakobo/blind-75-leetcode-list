
# Time complexity: O(n)
# Memory complexity: O(n)

def merge_intervals(intervals: list[tuple[int]]) -> list[tuple[int]]:

    def func(obj):
        return obj[0]

    # Time Complexity: O(nlogn)
    intervals.sort(key = func)
    print("Array:", intervals)

    output = [intervals[0]] 

    for start, end in intervals[1:]:
        start_prev, end_prev = output[-1]  # Most recent interval    
        
        if start <= end_prev:
            # output.pop()
            # output.append( (start_prev, end) )
            output[-1][1] = max(end, end_prev)
        else:
            output.append( (start, end) )

    return output

# nums = [[1, 3], [8, 10], [15, 18], [2, 6]]
nums = [ [1, 10], [2, 5], [7, 8], [1, 6]]

print(merge_intervals(nums))