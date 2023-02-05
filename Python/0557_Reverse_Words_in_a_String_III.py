class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        q = deque([])
        str = ""
        i = 0
        while i < len(s):
            if s[i] != ' ':
                q.append(s[i])
            else:
                while len(q) > 0:
                    str += q.pop()
                str += " "
            i += 1
        while len(q) > 0:
            str += q.pop()
        return str
        