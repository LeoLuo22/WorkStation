class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        nums = []
        for i in range(0, n):
            nums.append(True)
        nums[0] = False
        res = 0
        limit = int(math.sqrt(n))
        for i in range(2, limit + 1):
            if(nums[i]):
                for j in range(i * i, n, i):
                    nums[j] = False
        for k in range(0, n):
            if(nums[k]):
                res += 1

        return res - 1
