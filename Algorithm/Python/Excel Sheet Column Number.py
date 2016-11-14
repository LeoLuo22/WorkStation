class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        result = 0
        trans = 0
        j = 0
        for i in range(len(s) - 1, -1, -1):
            trans = (alpha.index(s[i]) + 1) * (26 ** j)
            result += trans
            j += 1
        return result

solution = Solution()
print(solution.titleToNumber("AAA"))
