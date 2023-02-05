/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let snowball = 0;
    for(let i=0; i<nums.length; i++) {
        if(nums[i] == 0) {
            snowball++;
        }
        else if(snowball > 0) {
            nums[i-snowball] = nums[i];
            nums[i] = 0; 
        }
    }
};