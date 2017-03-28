class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nan = float('nan')
        diffs = [a - b for a, b in zip([nan] + nums, nums + [nan]) if a - b]
        return sum(not d * e >= 0 for d, e in zip(diffs, diffs[1:]))
