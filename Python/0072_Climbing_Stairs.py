class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1 or n == 2 or n == 3:
            return n
        else:
            arr = [1, 2, 3]
            for i in range(2, n-1):
                arr.append(arr[-1] + arr[-2])
            return arr[n-1]