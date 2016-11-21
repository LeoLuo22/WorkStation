class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        begin = 0
        end = (x + 1) // 2
        mid = 0
        tmp = 0
        while(begin < end):
            mid = begin + (end - begin) // 2
            tmp = mid * mid
            if(tmp == x):
                return mid
            elif tmp < x:
                begin = mid + 1
            else:
                end = mid - 1
        tmp = end * end
        if(tmp > x):
            return end - 1
        else:
            return end

#52ms
