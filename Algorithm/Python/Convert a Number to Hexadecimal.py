class Solution(object):
    def toHex(self, num):
        max_dec = 4294967296
        if num < 0:
            num = max_dec - abs(num)
        s = "0123456789abcdef"
        rst = []
        mo = 0
        yu = num
        while(num >= 16):
            mo = num % 16
            yu = num // 16
            rst.append(mo)
            num = yu
        rst.append(yu)
        result = ""
        for i in range(len(rst)-1, -1, -1):
            result += s[rst[i]]
        return result

#35ms
