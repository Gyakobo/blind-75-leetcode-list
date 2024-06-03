/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    // Pretty much a Set but probably with overhead
    let d = {};
    for (let i in nums) {
        if (nums[i] in d) return true;
        d[nums[i]] = 1;
    }
    return false;
};