class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        result = []
        strs.sort()
        minlen = min(len(strs[0]), len(strs[-1]))
        for i in range(minlen):
            if strs[0][i] == strs[-1][i]:
                result.append(strs[0][i])
            else:
                return ''.join(result)
        return ''.join(result)