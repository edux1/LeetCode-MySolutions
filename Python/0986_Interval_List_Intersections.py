class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        i, j = 0, 0
        pi, pj = 0, 0
        res = []
        while i < len(firstList) and j < len(secondList):
            if (firstList[i][1] >= secondList[j][0] and firstList[i][1] <= secondList[j][1]) or (firstList[i][0] <= secondList[j][1] and firstList[i][1] >= secondList[j][1]):
                res.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])])
                if firstList[i][1] < secondList[j][1]:
                    i += 1
                elif firstList[i][1] > secondList[j][1]:
                    j += 1
                else:
                    i += 1
                    j += 1
            else:
                if firstList[i][1] < secondList[j][1]:
                    i += 1
                elif firstList[i][1] > secondList[j][1]:
                    j += 1
                else:
                    i += 1
                    j += 1
        
        return res