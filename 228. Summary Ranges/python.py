class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 1:
            return [str(nums[0])]
        
        res, i = [], 0
        
        while i < len(nums):
            a = nums[i]
            while i + 1 < len(nums) and nums[i] + 1 == nums[i+1]:
                i += 1
                
            if nums[i] != a:
                res.append(str(a)+'->'+str(nums[i]))
            else:
                res.append(str(a))
            i += 1
        return res                        