/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let l = 0;
    let r = nums.length-1;
    let mid;
    while(l <= r) {
        mid = Math.round((l + r) / 2);
        if(nums[mid] < target) {
            l = mid + 1;
        }
        else if(nums[mid] > target) {
            r = mid - 1;
        }
        else {
            return mid;
        }
    }
    return -1;
};