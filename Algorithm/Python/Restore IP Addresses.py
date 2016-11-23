class Solution:

    def doRestoreIpAddresses(self, prefix, num, s, start, fields):
        if start == len(s) - 1:
            results1 = [ ]
            results2 = [ ]
            if int(num + s[start]) <= 255 and 3 == fields and '0' != num:
                results1 = [prefix + s[start]]
            elif 2 == fields:
                results2 = [prefix + '.' + s[start]]
            return results1 + results2
        if int(num + s[start]) <= 255:
            results0 = [ ]
            results1 = [ ]
            if fields < 3:
                results0 = self.doRestoreIpAddresses(prefix + '.' + s[start], s[start], s, start + 1, fields + 1)
            if '0' != num:
                results1 = self.doRestoreIpAddresses(prefix + s[start], num + s[start], s, start + 1, fields)
            return results0 + results1
        elif fields < 3:
            results0 = self.doRestoreIpAddresses(prefix + '.' + s[start], s[start], s, start + 1, fields + 1)
            return results0
        else:
            return [ ]

    def restoreIpAddresses(self, s):
        if len(s) < 4:
            return [ ]
        return self.doRestoreIpAddresses(s[0], s[0], s, 1, 0)
