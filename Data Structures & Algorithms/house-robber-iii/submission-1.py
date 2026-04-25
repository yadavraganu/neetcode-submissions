# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    cache = {None:0}
    def rob(self, root: Optional[TreeNode]) -> int: 
        if root in self.cache:
            return self.cache[root]
        res = root.val
        if root.left:
            res += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            res += self.rob(root.right.left) + self.rob(root.right.right)
        res = max(res,self.rob(root.left) + self.rob(root.right))
        self.cache[root] = res
        return res