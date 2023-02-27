class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        sol = 0
        for i in range(32):
            if 1 & n:
                sol += 1
            if i != 31:
                sol <<= 1
                n >>= 1

        return sol