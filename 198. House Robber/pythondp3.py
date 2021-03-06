class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev = cur = 0
        for i in nums:
            prev, cur = cur, max(prev + i, cur)
        return cur
        