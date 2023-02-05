class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ant = 1000;
        res = 0;
        for c in s:
            if c == "I":
                value = 1;
            elif c == "V":
                value = 5;
            elif c == "X":
                value = 10;
            elif c == "L":
                value = 50;
            elif c == "C":
                value = 100;
            elif c == "D":
                value = 500;
            elif c == "M":
                value = 1000;
            res += value;
            if value > ant:
                res -= ant*2;
            ant = value;
        return res;
        