class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Time Complexity: O(log N)
        # Space Complexity: O(1)
        cnt = 0
        while num > 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            cnt += 1
        return cnt