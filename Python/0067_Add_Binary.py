class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Time Complexity: O(max(N, M))
        # Space Complexity: O(max(n, M))
        res = ""
        i, j = len(a)-1, len(b)-1
        carry = 0

        while i >= 0 or j >= 0 or carry > 0:
            sum = carry
            if i >= 0:
                sum += int(a[i])
                i -= 1
            if j >= 0:
                sum += int(b[j])
                j -= 1
            res += str(sum % 2)
            carry = sum // 2
            
        return res[::-1]