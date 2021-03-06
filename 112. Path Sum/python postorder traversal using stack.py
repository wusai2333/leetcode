# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        s = []
        pre, cur = None, root
        SUM = 0
        while cur or s:
            while cur:
                s.append(cur)
                SUM += cur.val
                cur = cur.left
            cur = s[-1]
            if cur.left == None and cur.right == None and SUM == sum:
                return True
            if cur.right and pre != cur.right:
                cur = cur.right
            else:
                pre = cur
                s.pop()
                SUM -= cur.val
                cur = None
        return False