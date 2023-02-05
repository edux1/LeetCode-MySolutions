/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
    let l = 0;
    let r = nums.length - 1;
    let sol = [];
    while(l <= r) {
        if(nums[l]**2 >= nums[r]**2) {
            sol.unshift(nums[l]**2);
            l++;
        }
        else {
            sol.unshift(nums[r]**2);
            r--;
        }
    }
    return sol;
};