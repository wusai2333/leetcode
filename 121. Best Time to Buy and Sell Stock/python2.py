class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        minPrice = sys.maxsize
        for p in prices:
            minPrice = min(p, minPrice)
            maxProfit = max(maxProfit, p - minPrice)
        return maxProfit
            
            