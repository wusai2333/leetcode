class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[1]]
        for _ in range(1, numRows):
            result += [map(lambda x,y: x + y, result[-1] + [0], [0] + result[-1])]
        return result[:numRows]

explanation: Any row can be constructed using the offset sum of the previous row. Example:

    1 3 3 1 0 
 +  0 1 3 3 1
 =  1 4 6 4 1

result[:numRows] is used to handle the case when numRows == 0 to return the [] not the [[1]]