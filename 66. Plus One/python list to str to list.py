<<<<<<< HEAD
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for i in range(len(digits)):
            num = num*10 + digits[i]
        return [int(i) for i in str(num+1)]

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for i in range(len(digits)):
            num = reduce(lambda x, y: 10*x+y, digits) + 1
        return [int(i) for i in str(num)]
=======
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for i in range(len(digits)):
            num = num*10 + digits[i]
        return [int(i) for i in str(num+1)]

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for i in range(len(digits)):
            num = reduce(lambda x, y: 10*x+y, digits) + 1
        return [int(i) for i in str(num)]
>>>>>>> origin/master
            