class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time Complexity: O(N)
        # Space Complexity: O(1)
        n = len(nums)

        if n < 3:
            return 0
        
        previous_difference = 0
        count = 0
        elements = 1

        for i in range(1, n):
            difference = nums[i] - nums[i-1]
            
            if i == 1 or previous_difference == difference:
                elements += 1
            else:
                if elements >= 3:
                    sum_elements = 0
                    for j in range(1, elements-1):
                        sum_elements += j
                    count += sum_elements
                elements = 2
            previous_difference = difference

        if elements >= 3:
            sum_elements = 0
            for j in range(1, elements-1):
                sum_elements += j
            count += sum_elements
            
        return count
