# Find Minimum in Rotated Sorted Array

Suppose an array of length n sorted in ascending order is rotated
between 1 and n times. For example, the array nums=[0, 1, 2, 4, 5, 6, 7]
might become:

```python
[4, 5, 6, 7, 0, 1, 2] # if it was rotated 4 times
[0, 1, 2, 4, 5, 6, 7] # if it was rotated 7 times
```

Notice that rotating an array `[a[0], a[1], a[2], ..., a[n-1]]` 1 time results in the array `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given the sorted rotated array nums of *unique* elements, return the minimum element of this array.

>[!Note]
>You could of course implement a simple for loop algorithm that gives an answer in O(n) time complexity, but you must write an algorithm that runs in O(log n) time.

A valid solution would be two use *3 pointers*