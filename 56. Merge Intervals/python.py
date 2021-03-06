# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0: return []
        intervals.sort(key = lambda interval: interval.start)
        res = [intervals[0]]
        for n in intervals[1:]:
            if n.start <= res[-1].end: 
                res[-1].end = max(res[-1].end, n.end)
            else: 
                res += i,
        return res
        
Sort the list first. Check if the new interval overlaps with the previous one in the output list. If yes, update it. Otherwise, append the new one.
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0: return []
        out = []
        for i in sorted(intervals, key = lambda x: x.start):
            if out and i.start <= out[-1].end:
                out[-1].end = max(out[-1].end, i.end)
            else:
                out += i,
        return out
        