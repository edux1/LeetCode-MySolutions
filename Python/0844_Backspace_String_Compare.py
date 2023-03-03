class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        it1, it2 = len(s)-1, len(t)-1
        skip1, skip2 = 0, 0
        while it1 >= 0 and it2 >= 0:
            if s[it1] == '#':
                skip1 = 1
                it1 -= 1
                while s[it1] == '#' or it1 >= 0 and skip1 > 0:
                    if s[it1] != '#':
                        skip1 -= 1
                    else:
                        skip1 += 1
                    it1 -= 1

            if t[it2] == '#':
                skip2 = 1
                it2 -= 1
                while t[it2] == '#' or it2 >= 0 and skip2 > 0:
                    if t[it2] != '#':
                        skip2 -= 1
                    else:
                        skip2 += 1
                    it2 -= 1
            
            if it1 < 0 and it2 < 0:
                return True
            elif it1 >= 0 and it2 >= 0:
                if s[it1] != t[it2]:
                    return False
                else:
                    it1 -= 1
                    it2 -= 1
            else:
                return False

        if it1 >= 0:
            if s[it1] != '#':
                return False
            while s[it1] == '#' or it1 >= 0 and skip1 > 0:
                if s[it1] != '#':
                    skip1 -= 1
                else:
                    skip1 += 1
                it1 -= 1
        if it2 >= 0:
            if t[it2] != '#':
                return False
            while t[it2] == '#' or it2 >= 0 and skip2 > 0:
                if t[it2] != '#':
                    skip2 -= 1
                else:
                    skip2 += 1
                it2 -= 1

        return True