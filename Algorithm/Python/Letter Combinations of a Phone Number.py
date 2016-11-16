class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []
        if len(digits) == 0:
            return result
        phone = [[],[],['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], ['p','q','r','s'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        tmp = ""
        rst = []
        for key in phone[int(digits[0])]:
            rst.append(key)
        if len(digits) == 1:
            return rst
        another = []
        for n in range(1, len(digits)):
            for i in range(0, len(rst)):
            #for j in range(0, len(phone[int(digits[1])])):
                for j in range(0, len(phone[int(digits[n])])):
                    tmp = rst[i]
                    tmp += phone[int(digits[n])][j]
                    another.append(tmp)
                    if len(tmp) == len(digits):
                        result.append(tmp)
            rst = another
        return result
        #86ms
