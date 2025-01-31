
def merge_intervals(intervals: List[Tuple[int]]) -> List[Tuple[int]]:
    def func(obj):
        return obj[0] 

    # Time complexity of sorting: 0(nlogn)     
    intervals.sort(key = func)
    output = [intervals[0]]    

    for start, end in intervals[1:]:
        


    return output

nums = [(1, 3), (8, 10), (15, 18), (2, 6)]
