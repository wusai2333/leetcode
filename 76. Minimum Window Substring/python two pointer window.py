<<<<<<< HEAD
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = collections.defaultdict(int)
        # statistic for count of char in t
        for c in t: dic[c] += 1
        counter, start, end = len(t), 0, 0
        d = sys.maxsize
        head = 0
        # move end to find a valid window
        while end < len(s):
            # if char in s exists in t, decrease counters
            if dic[s[end]] > 0: counter -= 1 # in t
            dic[s[end]] -= 1
            end += 1
            # we found a valid window, move start to find smaller window
            while counter == 0: # valid
                if end - start < d:
                    head = start
                    d = end - start
                dic[s[start]] += 1
                # when char exist in t, increase the counter
                if dic[s[start]] > 0:
                    counter += 1
                start += 1
        if d != sys.maxsize:
            return s[head: head+d]
        return ""
                
=======
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = collections.defaultdict(int)
        # statistic for count of char in t
        for c in t: dic[c] += 1
        counter, start, end = len(t), 0, 0
        d = sys.maxsize
        head = 0
        # move end to find a valid window
        while end < len(s):
            # if char in s exists in t, decrease counters
            if dic[s[end]] > 0: counter -= 1 # in t
            dic[s[end]] -= 1
            end += 1
            # we found a valid window, move start to find smaller window
            while counter == 0: # valid
                if end - start < d:
                    head = start
                    d = end - start
                dic[s[start]] += 1
                # when char exist in t, increase the counter
                if dic[s[start]] > 0:
                    counter += 1
                start += 1
        if d != sys.maxsize:
            return s[head: head+d]
        return ""
                
>>>>>>> origin/master
if we use a list = [0]*128 other than dict, it will be faster