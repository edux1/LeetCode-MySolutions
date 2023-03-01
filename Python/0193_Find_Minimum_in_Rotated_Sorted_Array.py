class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r)/2
            if nums[l] != nums[mid]:
                if nums[l] < nums[mid]:
                    if nums[l] < nums[r]:
                        return nums[l]
                    else:
                        l = mid + 1
                else:
                    r = mid
            else:
                if nums[l] <= nums[r]:
                    return nums[l]
                else:
                    return nums[r]
        return nums[l]