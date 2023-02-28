class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r)/2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if nums[l] < target:
            l += 1

        if len(nums) <= l or l < 0 or nums[l] != target:
            return [-1,-1]
        
        ll, r = l, len(nums)-1
        while ll < r:
            mid = (ll+r)/2
            if nums[mid] > target:
                r = mid - 1
            else:
                ll = mid + 1
        if nums[r] > target:
            r -= 1
        
        return [l, r]