class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        sign = -1 if x<0 else 1
        x = abs(x)
        while x!=0:
            tail = x % 10
            newResult = result * 10 + tail
            if newResult >= 0x7FFFFFFF:
                return 0
            result = newResult
            x /= 10
        return result*sign 