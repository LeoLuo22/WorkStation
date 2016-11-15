class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        after = self.generator("1")
        begin = self.generator("1")
        for i in range(0, n - 2):
            after = self.generator(begin)
            begin = after
        return after

    def generator(self, begin):
        count = 1
        result = ""
        tmp = begin[0]
        for i in range(0, len(begin)):
            if i == len(begin) - 1:
                return result + str(count) + begin[i]
            else:
                if tmp == begin[i + 1]:
                    count += 1
                else:
                    result = result + str(count) + tmp
                    tmp = begin[i + 1]
                    count = 1
#69ms

