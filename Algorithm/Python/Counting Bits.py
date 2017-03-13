class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = []
        count = 0
        for i in range(0, num+1):
            bin_i = bin(i)
            for num in bin_i:
                print(num, end=" ")
                if num == '1':
                    count += 1
            result.append(count)
            count = 0
        return result
