## LeetCode Questions
#


> # Two Sum
* Given an array of integers **nums** and an integer target, return indices of the two numbers such that they add up to **target**.
* You may assume that each input would have exactly one solution, and you may not use the same element twice. 
* You can return the answer in any order
* Keep in mind that the given array is ordered

### Example 1
```
Input: nums = [2, 7, 11, 15], target=9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]
```

### Example 2
```
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
```
### Example 3
```
Input: nums = [3, 3], target = 6
Output: [0, 1]
```


### CPP Implementation
```cpp
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> return_vector;
        int a_pointer = 0;
        int b_pointer = nums.size() - 1;

        while (a_pointer <= b_pointer) {
            int sum = nums[a_pointer] + nums[b_pointer];

            if (sum > target) b_pointer -= 1;
            else if (sum < target) b_pointer += 1;
            else {
                return_vector.push_back(a_pointer)
                return_vector.push_back(b_pointer);
                return return_vector;
            }
        } 

        return_vector.push_back(a_pointer)
        return_vector.push_back(b_pointer);
        return return_vector;
    }
}
```

### Java Implementation
```java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int a_pointer = 0;
        int b_pointer = nums.length - 1;

        while (a_pointer <= b_pointer) {
            int sum = nums[a_pointer] + nums[b_pointer]; 

            if (sum > target) {
                b_pointer -= 1;
            } 
            
            else if (sum < target) {
                a_pointer += 1;
            } 
            
            else {
                return new int[] {a_pointer, b_pointer};
            }
        }

        return new int[] {a_pointer, b_pointer};
    }
}
```

### Python Implementation
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a_pointer = 0
        b_pointer = len(nums) - 1

        while (a_pointer <= b_pointer):
            sum = nums[a_pointer] + nums[b_pointer]

            if (sum > target):
                b_pointer -= 1
            elif (sum < target):
                a_pointer += 1    
            else:
                return [a_pointer, b_pointer]

        return [a_pointer, b_pointer]
```
